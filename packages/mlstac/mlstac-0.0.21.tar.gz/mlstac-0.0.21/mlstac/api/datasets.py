import pathlib

import safetensors
from mlstac.api.utils import base61_encode, simple_download_extract, urljoin


class LocalDataset:
    def __init__(
        self, path: pathlib.Path, framework: str = "torch", device: str = "cpu"
    ):
        self.path = path
        self.files = list(path.glob("*.safetensors"))
        self.framework = framework
        self.device = device

    def __getitem__(self, index):
        tensors = {}
        with safetensors.safe_open(
            filename=self.files[index], framework=self.framework, device=self.device
        ) as f:
            for k in f.keys():
                tensors[k] = f.get_tensor(k)
            return tensors

    def __len__(self):
        return len(self.files)


class StreamDataset:
    def __init__(
        self,
        url: str,
        tempfile: pathlib.Path,
        framework: str = "torch",
        device: str = "cpu",
    ):
        self.framework = framework
        self.device = device
        self.url = url
        self.tempfile = tempfile

    def __getitem__(self, index):
        file_snippet = base61_encode(index).zfill(7)

        url_file = urljoin(self.url, "%s.safetensors.gz" % file_snippet)

        simple_download_extract(url_file, self.tempfile)
        tensors = {}
        with safetensors.safe_open(
            filename=self.tempfile, framework=self.framework, device=self.device
        ) as f:
            for k in f.keys():
                tensors[k] = f.get_tensor(k)
            return tensors

    def __len__(self):
        return len(self.files)
