import pathlib

from mlstac.sample.datamodel import Sample, SampleMetadata, SampleTensor
from mlstac.collection.datamodel import Collection
from mlstac.api.main import load, download
from mlstac.api.datasets import LocalDataset, StreamDataset

from mlstac.api.nest_asyncio import apply as nest_asyncio_apply
from typing import Union

# Patch asyncio to make its event loop reentrant.
nest_asyncio_apply()


# Huggingface utils
def hf_getlink(repoinfo, path: Union[str, pathlib.Path]):
    """ Get the link to a file in a Huggingface dataset repository.
    Args:
        repoinfo (str): The repository name.
        path (Union[str, pathlib.Path]): The path to the file.
    """
    if isinstance(path, str):
        path = pathlib.Path(path)
    
    return {
        "n_items": len(list(path.glob("*.safetensors.gz"))),
        "link": f"{str(repoinfo)}/resolve/main/{path.stem}/",
    }
