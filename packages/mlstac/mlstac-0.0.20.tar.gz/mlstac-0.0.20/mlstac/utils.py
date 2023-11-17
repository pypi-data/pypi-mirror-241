import gzip
import json
import pathlib
import re
import struct
from typing import Any, Generator, List, Union
import tempfile
import hashlib
import torch
import tqdm
import pickle
import polars

# Base61 encoding --------------------------------------------
BASE_ALPH = tuple("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
BASE_DICT = dict((c, v) for v, c in enumerate(BASE_ALPH))
BASE_LEN = len(BASE_ALPH)


def base61_encode(num: int) -> str:
    """ Encode a number in base61.
    Args:
        num (int): The number to encode.
    Returns:
        str: The encoded string.
    """
    if not num:
        return BASE_ALPH[0]
    encoding = ""
    while num:
        num, rem = divmod(num, BASE_LEN)
        encoding = BASE_ALPH[rem] + encoding
    return encoding

# General utils --------------------------------------------

def finder(
    path: str, pattern: str = None, full_names: bool = False, recursive: bool = False
) -> List[str]:
    """
    Returns a sorted list of file paths in the given directory.

    Args:
        path (str): The directory path to search for files.
        pattern (str, optional): A pattern to match file names against. Defaults to None.
        full_names (bool, optional): Whether to return full file paths or just file names. Defaults to False.
        recursive (bool, optional): Whether to search for files recursively. Defaults to False.

    Returns:
        List[str]: A sorted list of file paths or names.
    """
    files = list(list_file_gen(path, pattern, full_names, recursive))
    files_str = [str(file) for file in files]
    files_str.sort()
    return files_str


def list_file_gen(
    path: Union[str, pathlib.Path],
    pattern: str = None,
    full_names: bool = False,
    recursive: bool = False,
) -> Generator[Union[pathlib.Path, str], None, None]:
    """
    Returns a generator of file paths or names in the given directory.

    Args:
        path (Union[str, pathlib.Path]): The directory path to search for files.
        pattern (str, optional): A pattern to match file names against. Defaults to None.
        full_names (bool, optional): Whether to return full file paths or just file names. Defaults to False.
        recursive (bool, optional): Whether to search for files recursively. Defaults to False.

    Yields:
        Generator[Union[pathlib.Path, str], None, None]: A generator of file paths or names.
    """
    path = pathlib.Path(path)
    for file in path.iterdir():
        if file.is_file():
            if pattern is None:
                if full_names:
                    yield file
                else:
                    yield file.name
            elif pattern is not None:
                regex_cond = re.compile(pattern=pattern)
                if regex_cond.search(str(file)):
                    if full_names:
                        yield file
                    else:
                        yield file.name
        elif recursive:
            yield from list_file_gen(file, pattern, full_names, recursive)


# Metadata parquet utils --------------------------------------------
def read_metadata_safetensor(
    file: Union[str, pathlib.Path], compress: bool = True
) -> dict:
    """ Reads the metadata of a SafeTensor dataset.

    Args:
        file (Union[str, pathlib.Path]): The file path to the dataset.
        compress (bool, optional): Whether the dataset is compressed. Defaults to True.

    Returns:
        dict: A dictionary containing the metadata of the dataset.    
    """

    if isinstance(file, str):
        file = pathlib.Path(file)

    if compress:
        with gzip.open(file, "rb") as f:
            data = f.read()
    else:
        with open(file, "rb") as f:
            data = f.read()

    # Get the metadata of the dataset
    length_of_header = struct.unpack("<Q", data[:8])[0]
    metadata = json.loads(data[8 : 8 + length_of_header])

    # Save the metadata
    metadata_dict = metadata.pop("__metadata__")
    for key, value in metadata.items():
        metadata_dict[key + "__dtype"] = value["dtype"]
        metadata_dict[key + "__shape"] = "[%s]" % ", ".join(
            [str(i) for i in value["shape"]]
        )
        metadata_dict[key + "__offset"] = "[%s]" % ", ".join(
            [str(i) for i in value["data_offsets"]]
        )

    return metadata_dict


def create_parquet(
        path: Union[str, pathlib.Path],
        checksum: bool = True,
        num_workers: int = 0,
        verbose: bool = True
):
    if isinstance(path, str):
        path = pathlib.Path(path)

    splits = ["train", "validation", "test"]
    for split in splits:            
        # Create the dataset
        tdataset = CreateParquetFromSafeTensor(
            path=path / split,
            checksum=checksum
        )
        
        # Define the concurrent workers
        datamodule = DataModule(
            dataset=tdataset,
            num_workers=num_workers,
            message=f"Processing {split}",
            verbose=verbose
        )
        
        # Create metadata using several workers
        datamodule()
        
        # Enter to the temp folder where the metadata is stored
        datafolder = pathlib.Path(datamodule.dataset.tmp_dir.name)

        # Function to read the metadata
        def func(x):
            with open(x, "rb") as f:
                metadata = pickle.load(f)
            return metadata
        
        # Read the metadata concurrently
        merged_file = runrun(
            function=func,
            iterable=list(datafolder.glob("*.pkl")),
            num_workers=num_workers,
            message=f"Reading {split} metadata",
            verbose=verbose
        )

        # Merge the metadata and save it
        polars.DataFrame(merged_file).write_parquet(
            path / f"{split}.parquet"
        )
    return None


class CreateParquetFromSafeTensor:
    def __init__(
        self,
        path: Union[str, pathlib.Path],
        checksum: bool = True
    ):
        self.checksum = checksum
        self.path = pathlib.Path(path)
        self.files = finder(
            path=path,
            pattern=".*safetensors\.gz$",
            recursive=True,
            full_names=True,
        )
        self.files.sort()

        # create a folder in the temp directory
        self.tmp_dir = tempfile.TemporaryDirectory()
    
    def __len__(self):
        return len(self.files)
    
    def __getitem__(self, idx):
        file = self.files[idx]
        file_id = pathlib.Path(pathlib.Path(file).stem).stem
        metadata_f = read_metadata_safetensor(file)
        
        if self.checksum:
            with open(file, "rb") as f:
                checksum = hashlib.md5(f.read()).hexdigest()
            metadata_f["_checksum"] = checksum

        ## save the metadata using pickle
        with open("%s/%s.pkl" % (self.tmp_dir.name, file_id), "wb") as f:
            pickle.dump(metadata_f, f)
        return True


# DataModule utils --------------------------------------------
class DataModule:
    def __init__(
            self,
            dataset: torch.utils.data.Dataset,
            num_workers: int = 0,            
            message: str = "Processing dataset...",
            verbose: bool = True            
        ):
        super().__init__()
        self.dataset = dataset
        self.message = message
        self.num_workers = num_workers
        self.verbose = verbose

    def run_dataloader(self) -> torch.utils.data.DataLoader:
        return torch.utils.data.DataLoader(
            dataset=self.dataset,
            batch_size=1,
            num_workers=self.num_workers
        )

    def __call__(self) -> Any:
        # Create the dataloader
        dataloader = self.run_dataloader()

        # Run the dataloader
        container = []
        if self.verbose:
            with tqdm.tqdm(total=len(self.dataset)) as pbar:
                pbar.set_description(self.message)                
                for x in dataloader:
                    pbar.update(1)
                    container.append(x)
        else:
            for x in dataloader:
                container.append(x)
        return container

def runrun(
    function,
    num_workers: int = 0,
    iterable: List[Any] = None,
    message: str = "Processing",
    verbose: bool = True,
):
    """ Run a function in parallel.
    Args:
        function (function): The function to run.
        num_workers (int, optional): The number of workers to use. Defaults to 0.
        iterable (List[Any], optional): The iterable to use. Defaults to None.
    """
    class Wrapper:
        def __init__(self, function, iterable):
            self.function = function
            self.iterable = iterable
        
        def __len__(self):
            return len(self.iterable)
        
        def __getitem__(self, idx):
            return [self.function(self.iterable[idx])]
        
    compressed = DataModule(
        dataset=Wrapper(function, iterable),
        num_workers=num_workers,
        message=message,
        verbose=verbose
    )

    return [x[0] for x in compressed()]