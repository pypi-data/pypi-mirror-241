import gzip
import hashlib
import importlib
import pathlib
import re
import warnings
from datetime import datetime
from tempfile import NamedTemporaryFile
from typing import Any, Optional
from mlstac.utils import base61_encode as _base61_encode
import pydantic



class SampleTensor(pydantic.BaseModel):
    # Fields -------------------------------------------------
    input: Any = None
    target: Any = None
    extra: Any = None
    tensor_framework: Optional[str] = None

    # Check Framework ----------------------------------------
    @classmethod
    def check_framework(cls, name: str) -> bool:
        try:
            importlib.import_module(name)
            return True
        except ModuleNotFoundError:
            return False

    @classmethod
    def check_is_a_tensor(cls, v: Any) -> bool:
        """ Check that the input is a valid tensor.

        Args:
            v (Any): The tensor to check. It can be a numpy, 
                torch, paddle, tensorflow or jax tensor.
        """

        np_ok = cls.check_framework("numpy")
        if np_ok:
            import numpy as np

            if type(v) == eval("np.ndarray"):
                cls._tensor_framework = "numpy"
                return True

        torch_ok = cls.check_framework("torch")
        if torch_ok:
            import torch

            if type(v) == eval("torch.Tensor"):
                cls._tensor_framework = "torch"
                return True

        jax_ok = cls.check_framework("jax")
        if jax_ok:
            import jax

            if type(v) == eval("jax.numpy.ndarray"):
                cls._tensor_framework = "jax"
                return True

        tensorflow_ok = cls.check_framework("tensorflow")
        if tensorflow_ok:
            import tensorflow

            if type(v) == eval("tensorflow.Tensor"):
                cls._tensor_framework = "tensorflow"
                return True

        paddle_ok = cls.check_framework("paddle")
        if paddle_ok:
            import paddle

            if type(v) == eval("paddle.Tensor"):
                cls._tensor_framework = "paddle"
                return True

        return False

    # Field Validators ---------------------------------------
    @pydantic.field_validator("input", "target", "extra")
    def check_target_and_extra(cls, v) -> None:
        if v is not None:
            if cls.check_is_a_tensor(v) is False:
                msg = "%s%s" % (
                    "The target or extra tensor must be None, ",
                    "or a numpy, torch, paddle or jax tensor.",
                )
                raise ValueError(msg)
        return v

    # Model Validators ---------------------------------------
    @pydantic.model_validator(mode="after")
    def check_model_none(self) -> "SampleTensor":
        if self.input is None:
            if self.target is None:
                if self.extra is None:
                    raise ValueError(
                        "The input, target and extra cannot all be None"
                    )
        return self

    @pydantic.model_validator(mode="after")
    def check_model_format(self) -> "SampleTensor":
        evaluation = "type(self.input)"
        if self.target is not None:
            evaluation = f"{evaluation} == type(self.target)"

        if self.extra is not None:
            evaluation = f"{evaluation} == type(self.extra)"

        if not eval(evaluation):
            raise ValueError(
                "The input, target and extra must be created with the same framework"
            )
        self.tensor_framework = self._tensor_framework
        return self


class SampleMetadata(pydantic.BaseModel):

    # Fields -------------------------------------------------
    id: int
    input: Optional[str] = None
    target: Optional[str] = None
    extra: Optional[dict] = None
    geotransform: Optional[list] = None
    crs: Optional[str] = None
    start_datetime: Optional[Any] = None
    end_datetime: Optional[Any] = None

    # Private Fields -----------------------------------------
    _safe_id: Optional[str] = pydantic.PrivateAttr()
    _safe_geotransform: Optional[str] = pydantic.PrivateAttr()
    _safe_start_datetime: Optional[str] = pydantic.PrivateAttr()
    _safe_end_datetime: Optional[str] = pydantic.PrivateAttr()

    # Field Validators ---------------------------------------
    @pydantic.field_validator("geotransform")
    def check_geotransform(cls, v: list) -> list:
        if len(v) != 6:
            raise ValueError("geotransform must contain 6 elements")

        if not all(isinstance(x, (int, float)) for x in v):
            raise ValueError("geotransform must contain only numbers")

        return v

    @pydantic.field_validator("crs")
    def check_crs(cls, v: str) -> str:
        regex_exp = re.compile(r"^(?:EPSG|ESRI|SR-ORG):[0-9]+$")

        if not regex_exp.match(v):
            raise ValueError("crs must be from the format: <authority>:<code>")

        return v

    @pydantic.field_validator("extra")
    def check_extra(cls, v: dict) -> dict:
        if not all(isinstance(x, (str, int, bool, float)) for x in v.values()):
            raise ValueError("extra only supports str, int, bool and float values")

        return v

    @pydantic.field_validator("start_datetime", "end_datetime")
    def check_datetime(cls, v: datetime) -> datetime:
        if not isinstance(v, datetime):
            raise ValueError("start_datetime and end_datetime must be datetime objects")

        return v

    # Model Validators ---------------------------------------
    @classmethod
    def base61_encode(cls, num: int) -> str:
        """ Encode a number in base61.

        Args:
            num (int): The number to encode.

        Returns:
            str: The encoded string.
        """
        return _base61_encode(num)

    @pydantic.model_validator(mode="after")
    def check_start_end_datetime(self) -> "SampleMetadata":
        if self.start_datetime is not None:
            if self.end_datetime is not None:
                if self.start_datetime > self.end_datetime:
                    raise ValueError("end_datetime must be after start_datetime")

        # Set the ID metadata
        self._safe_id = self.base61_encode(self.id).zfill(7)

        # Set the geotransform metadata
        if self.geotransform is not None:
            self._safe_geotransform = "[%s]" % " ,".join(
                [str(x) for x in self.geotransform]
            )
        else:
            self._safe_geotransform = None

        # Set the start_datetime metadata
        if self.start_datetime is not None:
            self._safe_start_datetime = self.start_datetime.isoformat()
        else:
            self._safe_start_datetime = None

        # Set the end_datetime metadata
        if self.end_datetime is not None:
            self._safe_end_datetime = self.end_datetime.isoformat()
        else:
            self._safe_end_datetime = None

        return self


class Sample(pydantic.BaseModel):
    tensor: SampleTensor
    metadata: SampleMetadata
    _filename: Optional[str] = pydantic.PrivateAttr()

    def save(self, path: str, compress: bool = True) -> None:
        """Save an ML-STAC sample to disk.

        Args:
            path (str): The path to save the sample to.
            compress (bool, optional): Whether to compress the sample
                using gzip. Defaults to True.
        """

        path = pathlib.Path(path)
        if not path.exists():
            warnings.warn(f"{path} does not exist. Creating it...")
            path.mkdir(parents=True, exist_ok=True)

        if compress:
            tmp_file = NamedTemporaryFile()
            filename = pathlib.Path(tmp_file.name)
            gz_filename = path / f"{self.metadata._safe_id}.safetensors.gz"
            self._filename = gz_filename
        else:
            filename = path / f"{self.metadata._safe_id}.safetensors"
            self._filename = filename

        # Prepare the required metadata ------------------------
        required_metadata = {"id": self.metadata._safe_id}
        if required_metadata["id"] is None:
            raise ValueError("The id cannot be None")

        # Prepare the Text metadata ----------------------------
        text_metadata = {"target": self.metadata.target, "input": self.metadata.input}

        text_metadata["isText"] = "1"
        if text_metadata["target"] is None:
            if text_metadata["input"] is None:
                text_metadata["isText"] = "0"
                text_metadata["input"] = ""
            text_metadata["target"] = ""

        # Prepare the STAC metadata ------------------
        geo_metadata = {
            "geotransform": self.metadata._safe_geotransform,
            "crs": self.metadata.crs,
            "start_datetime": self.metadata._safe_start_datetime,
            "end_datetime": self.metadata._safe_end_datetime,
        }

        geo_metadata["isSTAC"] = "1"
        if geo_metadata["geotransform"] is None:
            geo_metadata["geotransform"] = "[0 ,1 ,0 ,0 ,0 ,1]"
            geo_metadata["isSTAC"] = "0"

        if geo_metadata["crs"] is None:
            geo_metadata["crs"] = "EPSG:4326"
            geo_metadata["isSTAC"] = "0"

        if geo_metadata["start_datetime"] is None:
            geo_metadata["start_datetime"] = "1970-01-01T00:00:00"
            geo_metadata["isSTAC"] = "0"

        if geo_metadata["end_datetime"] is None:
            geo_metadata["end_datetime"] = geo_metadata["start_datetime"]

        extra_metadata = self.metadata.extra

        # Merge all the metadata ------------------
        if extra_metadata is None:
            for k, v in extra_metadata.items():
                if not isinstance(k, str):
                    raise ValueError(
                        "The extra metadata keys:values must be string-to-string pairs"
                    )

            sample_metadata = {**required_metadata, **text_metadata, **geo_metadata}
        else:
            sample_metadata = {
                **required_metadata,
                **text_metadata,
                **geo_metadata,
                **extra_metadata,
            }

        # Prepare tensors ---------------------------
        tensors = self.tensor.model_dump()
        tensors = {k: v for k, v in tensors.items() if v is not None}
        tensor_framework = tensors.pop("tensor_framework")

        # Save the file ----------------------------------------
        if tensor_framework == "numpy":
            import safetensors.numpy

            safetensors.numpy.save_file(
                tensors, metadata=sample_metadata, filename=filename
            )
        elif tensor_framework == "torch":
            import safetensors.torch

            safetensors.torch.save_file(
                tensors, metadata=sample_metadata, filename=filename
            )
        elif tensor_framework == "paddle":
            import safetensors.paddle

            safetensors.paddle.save_file(
                tensors, metadata=sample_metadata, filename=filename
            )
        elif tensor_framework == "tensorflow":
            import safetensors.tensorflow

            safetensors.tensorflow.save_file(
                tensors, metadata=sample_metadata, filename=filename
            )
        elif tensor_framework == "jax":
            import safetensors.jax

            safetensors.jax.save_file(
                tensors, metadata=sample_metadata, filename=filename
            )

        if compress:
            with open(filename, "rb") as f_in:
                with gzip.open(gz_filename, "wb") as f_out:
                    f_out.writelines(f_in)
            tmp_file.close()

    def checksum(self) -> None:
        filename = self._filename

        if not filename.exists():
            raise FileNotFoundError(f"{filename} does not found")

        # Checksum
        with open(filename, "rb") as f:
            checksum = hashlib.md5(f.read()).hexdigest()

        return checksum
