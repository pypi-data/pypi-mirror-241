import gzip
import hashlib
import json
import pathlib
import random
import polars
import re
import shutil
import struct
from typing import Dict, List, Literal, Optional, Union

import pydantic
import requests
import validators
from mdutils import Html, MdUtils
from mlstac.collection.spectral import (_add_aster, _add_eo1_ali,
                                        _add_landsat1, _add_landsat2,
                                        _add_landsat3, _add_landsat4_mss,
                                        _add_landsat4_tm, _add_landsat5_mss,
                                        _add_landsat5_tm, _add_landsat7,
                                        _add_landsat8, _add_landsat9,
                                        _add_modis, _add_sentinel2)
from mlstac.collection.stac import Link, STACCollection
from mlstac.utils import finder, read_metadata_safetensor, create_parquet

KEY_ORDER = (
    "id",
    "type",
    "stac_version",
    "description",
    "links",
    "stac_extensions",
    "title",
    "keywords",
    "providers",
    "extent",
    "license",
    "ml_version",
    "ml_train",
    "ml_validation",
    "ml_test",
    "ml_task",
    "ml_labels",
    "ml_curator",
    "ml_authors",
    "ml_reviewers",
    "ml_dimensions",
    "ml_spectral",
    "ml_split_strategy",
    "ml_raw_data_url",
    "ml_discussion_url",
    "ml_size",
    "ml_metadata_train",
    "ml_metadata_validation",
    "ml_metadata_test",
)

# ML-STAC - Label extension ----------------------------
class Labels(pydantic.BaseModel):
    """ This extension provides a way to define the labels of a 
    dataset. Useful for TensorClassification, ObjectDetection and
    SemanticSegmentation tasks.

    Fields:
        labels (Dict[str, int]): A dictionary with the labels and 
            their corresponding index.
    """

    labels: Dict[str, int]


# STAC - Contact extension ----------------------------
class Info(pydantic.BaseModel):
    """Contact extension is part of the STAC extension.
    Info is a part of the Contact extension.
    """

    value: str
    roles: Optional[List[str]] = None

    @pydantic.field_validator("value")
    def check_value(cls, v):
        if not re.match(r"^\+[1-9]{1}[0-9]{3,14}$", v):
            if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", v):
                raise ValueError("value must be a valid email or phone number")
        return v


class Address(pydantic.BaseModel):
    """Contact extension is part of the STAC extension.
    Address is a part of the Contact extension.
    """

    deliveryPoint: Optional[List[str]] = None
    city: Optional[str] = None
    administrativeArea: Optional[str] = None
    postalCode: Optional[str] = None
    country: Optional[str] = None


class Contact(pydantic.BaseModel):
    """ Pydantic Contact extension from the STAC extension.
    More info: https://github.com/stac-extensions/contacts
    """

    name: str
    organization: str
    identifier: Optional[str] = None
    position: Optional[str] = None
    logo: Optional[Link] = None
    phones: Optional[List[Info]] = None
    emails: Optional[List[Info]] = None
    addresses: Optional[List[Address]] = None
    links: Optional[List[Link]] = None
    contactInstructions: Optional[str] = None
    roles: Optional[List[str]] = None


# ML-STAC - Authors extension ----------------------------
class Authors(pydantic.BaseModel):
    """This extension provides a way to define authors. Useful for
    measuring the quality of a dataset.

    Fields:
        authors (List[Contact]): A list of authors.
    """

    authors: Optional[List[Contact]] = None


# ML-STAC - Curators extension ----------------------------
class Curators(pydantic.BaseModel):
    """This extension provides a way to define curators. Useful for
    measuring the quality of a dataset.

    Fields:
        curators (List[Contact]): A list of curators.
    """

    curators: Optional[List[Contact]] = None


# ML-STAC - Reviewer extension ----------------------------
class Reviewer(pydantic.BaseModel):
    """This extension provides a way to define reviewers. Useful for
    measuring the quality of a dataset.

    Fields:
        name (str): Name of the reviewer.
        score (Literal[0, 1, 2, 3, 4, 5]): Score of the reviewer.
            The score must be between 0 and 5. Higher is better.
        url (str): A public url where to find more information about
            the review process. Usually is a link to a github issue.
    """

    reviewer: Contact
    score: Optional[Literal[0, 1, 2, 3, 4, 5]] = None


class Reviewers(pydantic.BaseModel):
    """This extension define a review process. Useful for
    measuring the quality of a dataset.
    """

    reviewers: Optional[List[Reviewer]] = None


# ML-STAC - TensorDimensions extension --------------------------------
class Dimension(pydantic.BaseModel):
    """ In the ML-STAC specification, the dimensions are equal between
    all the samples. This extension defines the dimensions of the samples
    for each SampleTensor.
    
    fields:
        axis (int): The axis of the dimension.
        description (Optional[str]): A description of the dimension.
    """

    axis: int
    name: Optional[str] = None
    description: Optional[str] = None


class Dimensions(pydantic.BaseModel):
    """ In the ML-STAC specification, the dimensions are equal between
    all the samples. This extension defines the dimensions of the samples
    for each SampleTensor.
    
    fields:
        dimensions (Dict[str, Dimension]): A dictionary with the dimensions
            of the samples. The key is the name of the dimension and the
            value is a Dimension object.
        dtype (Optional[str]): The data type of the samples. This field
            is defined automatically by the 'automatic_field' method from the
            Collection class.
        shape (Optional[List[int]]): The shape of the samples. This field
            is defined automatically by the 'automatic_field' method from the
            Collection class.
        offsets (Optional[List[int]]): The offsets of the samples. This field
            is defined automatically by the 'automatic_field' method from the
            Collection class.
    """

    dimensions: Optional[List[Dimension]] = None
    dtype: Optional[str] = None
    shape: Optional[List[int]] = None

    def append(self, dimension: Dimension):
        self.dimensions.append(dimension)
        return None


class TensorDimensions(pydantic.BaseModel):
    """ In the ML-STAC specification, the dimensions are equal between
    all the samples. This extension defines the dimensions of the samples
    for each SampleTensor.

    Field:
        input (Optional[Dimensions]): The dimensions of the input.
        target (Optional[Dimensions]): The dimensions of the target.
        extra (Optional[Dimensions]): The dimensions of the extra.
    """

    input: Optional[Dimensions] = None
    target: Optional[Dimensions] = None
    extra: Optional[Dimensions] = None


# ML-STAC - SpectralBand extension --------------------------------
class SpectralBand(pydantic.BaseModel):
    """ This extension provides a way to define the spectral bands of a
    dataset. Useful for Remote Sensing datasets.

    fields:
        band (str): The name of the band.
        index (Optional[int]): The index of the band.
        description (Optional[str]): A description of the band.
        unit (Optional[str]): The unit of the band.
        wavelengths (Optional[List[float]]): The wavelengths of the band.
            It must be a list of two floats. The first float is the minimum
            wavelength and the second float is the maximum wavelength.
    """

    name: str
    index: Optional[int]
    common_name: Optional[str] = None
    description: Optional[str] = None
    unit: Optional[str] = None
    center_wavelength: Optional[float] = None
    full_width_half_max: Optional[float] = None


class SpectralBands(pydantic.BaseModel):
    """ This extension provides a way to define the spectral bands of a
    dataset. Useful for Remote Sensing datasets.

    fields:
        bands (Dict[str, SpectralBand]): A dictionary with the spectral
            bands of the dataset. The key is the name of the band and the
            value is a SpectralBand object.
        axis (Optional[int]): The axis of the spectral bands.
        sensor (Optional[str]): The sensor of the spectral bands.        
    """

    bands: List[SpectralBand]
    axis: Optional[int] = None
    sensor: Optional[str] = None


# ML-STAC specification --------------------------------------------
class Split(pydantic.BaseModel):
    """ML-STAC Catalog dataclass."""

    n_items: int
    link: str

    @pydantic.field_validator("n_items")
    def n_items_must_be_valid(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("n_items must be positive")
        return value

    @pydantic.field_validator("link")
    def link_must_be_valid(cls, v: str) -> str:
        return str(pydantic.AnyHttpUrl(v))


class Collection(STACCollection):
    # STAC automatic fields -------------------------
    extent: Optional[Dict[str, Dict[str, List]]] = None
    links: Optional[List[Link]] = None

    # Required fields -------------------------------
    ml_version: str = "0.1.0"
    ml_train: Split
    ml_validation: Split
    ml_test: Split
    ml_task: List[
        Literal[
            "TensorClassification",
            "TensorRegression",
            "TensorSegmentation",
            "ObjectDetection",
            "TensorToTensor",
            "TensorToText",
            "TextToTensor",
        ]
    ]

    # Opt fields ------------------------------------
    ml_labels: Optional[Labels] = None
    ml_authors: Optional[Authors] = None
    ml_curators: Optional[Curators] = None
    ml_reviewers: Optional[Reviewers] = None
    ml_dimensions: Optional[TensorDimensions] = None
    ml_spectral: Optional[SpectralBands] = None
    ml_split_strategy: Optional[
        Literal["random", "stratified", "systematic", "other"]
    ] = None
    ml_raw_data_url: Optional[str] = None
    ml_discussion_url: Optional[str] = None
    ml_paper: Optional[str] = None

    # Automatic fields ------------------------------------
    ml_size: Optional[float] = None
    ml_metadata_train: Optional[str] = None
    ml_metadata_test: Optional[str] = None
    ml_metadata_validation: Optional[str] = None

    def add_labels(self, **kwargs: dict) -> None:
        """ This method adds the labels of the dataset. 
        Useful for TensorClassification, ObjectDetection and
        SemanticSegmentation tasks.
        """
        self.ml_labels = Labels(**kwargs)
        print("Labels added to self.ml_labels")
        return None

    def add_extension(self, extension: str) -> None:
        """ Add an STAC extension to the ML-STAC collection."""

        # add extension
        if self.stac_extensions is None:
            self.stac_extensions = [extension]
        else:
            self.stac_extensions.append(extension)

        # remove duplicates
        self.stac_extensions = list(set(self.stac_extensions))

        return None

    def add_curator(self, **kwargs: dict) -> None:
        """ This method adds the curators of the dataset.
        Useful for reporting errors or requesting changes.
        """

        # Get the previous curators
        if self.ml_curators is not None:
            dataset_curators = self.ml_curators.curators
        else:
            dataset_curators = []

        # Check if the curator is already defined
        if any([d.name == kwargs["name"] for d in dataset_curators]):
            for d in dataset_curators:
                if d.name == kwargs["name"]:
                    dataset_curators.remove(d)

        # Load and append the new curator
        new_contact = Contact(**kwargs)
        dataset_curators.append(new_contact)

        # Save the new curators
        self.ml_curators = Curators(curators=dataset_curators)

        # add contact stac extension if not already added
        self.add_extension(
            "https://stac-extensions.github.io/contacts/v0.1.1/schema.json"
        )

        print("Curator added to self.ml_curators")
        return None

    def add_author(self, **kwargs: dict) -> None:
        """ This method adds the authors of the dataset."""
        
        # Get the previous authors
        if self.ml_authors is not None:
            dataset_authors = self.ml_authors.authors
        else:
            dataset_authors = []

        # Check if the author is already defined
        if any([d.name == kwargs["name"] for d in dataset_authors]):
            for d in dataset_authors:
                if d.name == kwargs["name"]:
                    dataset_authors.remove(d)

        # Load and append the new author
        new_contact = Contact(**kwargs)
        dataset_authors.append(new_contact)

        # Save the new authors
        self.ml_authors = Authors(authors=dataset_authors)

        # add contact stac extension
        self.add_extension(
            "https://stac-extensions.github.io/contacts/v0.1.1/schema.json"
        )

        print("Author added to self.ml_authors")

        return None

    def add_reviewer(self, **kwargs: dict) -> None:
        """ This method adds reviewers to the dataset."""
        
        # Get the previous reviewers
        if self.ml_reviewers is not None:
            dataset_reviewers = self.ml_reviewers.reviewers
        else:
            dataset_reviewers = []

        if kwargs["score"] is None:
            raise ValueError("score must be a value between 0 and 5")

        score = kwargs.pop("score")

        # Check if the reviewer is already defined
        if any([d.reviewer.name == kwargs["name"] for d in dataset_reviewers]):
            for d in dataset_reviewers:
                if d.reviewer.name == kwargs["name"]:
                    dataset_reviewers.remove(d)

        # Load and append the new reviewer
        new_review = Reviewer(reviewer=kwargs, score=score)
        dataset_reviewers.append(new_review)

        # Save the new reviewers
        self.ml_reviewers = Reviewers(reviewers=dataset_reviewers)

        print("Reviewer added to self.ml_reviewers")

        return None

    def get_review_mean_score(self) -> float:
        """ This method returns the mean score of the reviewers."""
        if self.ml_reviewers is None:
            #raise ValueError("There are no reviewers")
            return None
        
        scores = [r.score for r in self.ml_reviewers.reviewers]
        return sum(scores) / len(scores)

    def add_paper(self, url: str):
        """ This method adds the paper of the dataset."""
        self.ml_paper = str(pydantic.AnyHttpUrl(url))
        print("Paper added to self.ml_discussion_url")
        return None

    def add_dimension(
        self, tensor: Literal["input", "target", "extra"], **kwargs: dict
    ) -> None:
        """ This method adds a dimensions for the input, target or 
        extra tensors (sample objects). """

        # check if the tensor is valid
        if tensor not in ["input", "target", "extra"]:
            raise ValueError("tensor must be 'input', 'target' or 'extra'")

        # Get the previous dimensions
        if self.ml_dimensions is not None:
            tensor_dimensions = self.ml_dimensions
        else:
            tensor_dimensions = TensorDimensions(
                input=Dimensions(dimensions=[]),
                target=Dimensions(dimensions=[]),
                extra=Dimensions(dimensions=[]),
            )

        init_dimensions = getattr(tensor_dimensions, tensor)

        # Check if the axis is already defined
        try:
            if any([d.axis == kwargs["axis"] for d in init_dimensions.dimensions]):
                for d in init_dimensions.dimensions:
                    if d.axis == kwargs["axis"]:
                        init_dimensions.dimensions.remove(d)
        except:
            pass

        # Load and append the new curator
        dimension = Dimension(**kwargs)
        init_dimensions.append(dimension)

        # Save the new dimensions
        setattr(tensor_dimensions, tensor, init_dimensions)

        self.ml_dimensions = tensor_dimensions
        print("Dimensions added to self.ml_dimensions")

        return None

    def add_spectral_band(self, **kwargs: dict) -> None:
        """ Add a spectral band to the dataset. """
        
        # Get the previous spectral bands
        if self.ml_spectral is not None:
            init_bands = self.ml_spectral.bands
        else:
            init_bands = []

        # Check if the axis is already defined
        if any([d.name == kwargs["name"] for d in init_bands]):
            for d in init_bands:
                if d.name == kwargs["name"]:
                    init_bands.remove(d)

        # Load and append the new curator
        band = SpectralBand(**kwargs)
        init_bands.append(band)

        # Save the new dimensions
        self.ml_spectral = SpectralBands(bands=init_bands)

        print("Dimensions added to self.ml_dimensions")

        return None

    def add_sentinel2(self, bands: str = "all"):
        self.ml_spectral = None
        _add_sentinel2(self, bands=bands)
        return None

    def add_landsat1(self, bands: str = "all"):
        self.ml_spectral = None
        _add_landsat1(self, bands=bands)
        return None

    def add_landsat2(self, bands: str = "all"):
        self.ml_spectral = None
        _add_landsat2(self, bands=bands)
        return None

    def add_landsat3(self, bands: str = "all"):
        self.ml_spectral = None
        _add_landsat3(self, bands=bands)
        return None

    def add_landsat4_mss(self, bands: str = "all"):
        self.ml_spectral = None
        _add_landsat4_mss(self, bands=bands)
        return None

    def add_landsat4_tm(self, bands: str = "all"):
        self.ml_spectral = None
        _add_landsat4_tm(self, bands=bands)
        return None

    def add_landsat5_mss(self, bands: str = "all"):
        self.ml_spectral = None
        _add_landsat5_mss(self, bands=bands)
        return None

    def add_landsat5_tm(self, bands: str = "all"):
        self.ml_spectral = None
        _add_landsat5_tm(self, bands=bands)
        return None

    def add_landsat7(self, bands: str = "all"):
        self.ml_spectral = None
        _add_landsat7(self, bands=bands)
        return None

    def add_landsat8(self, bands: str = "all"):
        self.ml_spectral = None
        _add_landsat8(self, bands=bands)
        return None

    def add_landsat9(self, bands: str = "all"):
        self.ml_spectral = None
        _add_landsat9(self, bands=bands)
        return None

    def add_eo1_ali(self, bands: str = "all"):
        self.ml_spectral = None
        _add_eo1_ali(self, bands=bands)
        return None

    def add_aster(self, bands: str = "all"):
        self.ml_spectral = None
        _add_aster(self, bands=bands)
        return None

    def add_modis(self, bands: str = "all"):
        self.ml_spectral = None
        _add_modis(self, bands=bands)
        return None

    def add_sensor(self, sensor: str):
        """ Add the sensor of the spectral bands."""
        if self.ml_spectral is None:
            raise ValueError("There are no spectral bands")

        self.ml_spectral = SpectralBands(
            bands=self.ml_spectral.bands, axis=self.ml_spectral.axis, sensor=sensor
        )

        print("Specral information added to self.ml_spectral")
        return None

    def add_raw_data_url(self, url: str):
        self.ml_raw_data_url = str(pydantic.AnyHttpUrl(url))
        print("Raw information added to self.ml_raw_data_url")
        return None

    def add_discussion_url(self, url: str):
        self.ml_discussion_url = str(pydantic.AnyHttpUrl(url))
        print("Discussion added to self.ml_discuss_url")
        return None

    def add_split_strategy(self, split_strategy: str):
        self.ml_split_strategy = split_strategy
        print("Split added to self.ml_split")
        return None

    def auto(
        self,
        path: Union[str, pathlib.Path],
        checksum: bool = True,
        verbose: bool = False,
        num_workers: int = 0,
    ):
        if isinstance(path, str):
            path = pathlib.Path(path)

        # Get the size of the dataset
        all_files = finder(
            path, pattern=".*safetensors\.gz$", recursive=True, full_names=True
        )
        rnum = random.randint(0, len(all_files))
        rtensor = all_files[rnum]

        # Get the metadata of the dataset
        with gzip.open(rtensor, "rb") as f_out:
            bdata = f_out.read()
            length_of_header = struct.unpack("<Q", bdata[:8])[0]
            metadata = json.loads(bdata[8 : 8 + length_of_header])

        # get the size of the dataset
        self.ml_size = round((len(bdata) / 1024 ** 3) * len(all_files), 4)

        # Get the dimensions of the dataset
        if self.ml_dimensions is not None:
            if len(self.ml_dimensions.extra.dimensions) != 0:
                self.ml_dimensions.extra.dtype = metadata["input"]["dtype"]
                self.ml_dimensions.extra.shape = metadata["input"]["shape"]

            if len(self.ml_dimensions.input.dimensions) != 0:
                self.ml_dimensions.input.dtype = metadata["input"]["dtype"]
                self.ml_dimensions.input.shape = metadata["input"]["shape"]

            if len(self.ml_dimensions.target.dimensions) != 0:
                self.ml_dimensions.target.dtype = metadata["target"]["dtype"]
                self.ml_dimensions.target.shape = metadata["target"]["shape"]

        # Add links
        self.create_link()

        # Save the metadata
        self.create_parquet(
            path=path,
            checksum=checksum,
            num_workers=num_workers,
            verbose=verbose
        )
        self.ml_metadata_train = str(path / "train/metadata.parquet")
        self.ml_metadata_validation = str(path / "validation/metadata.parquet")
        self.ml_metadata_test = str(path / "test/metadata.parquet")

        # Add extent
        self.create_extent(path=path)

        # Get the metadata of the dataset
        self.create_jsonfile(path=path)

        # Get the metadata of the dataset
        self.add_documentation(path=path)

        return None

    def create_link(self):
        self.links = [
            Link(**{"rel": "root", "href": "./main.json", "type": "application/json"})
        ]
        return None

    def create_bbox(self, dataset):
        for index, value in enumerate(dataset["geotransform"]):
            geotransform = eval(value)
            if index == 0:
                train_xmin, train_ymin, train_xmax, train_ymax = (
                    geotransform[0],
                    geotransform[3],
                    geotransform[0],
                    geotransform[3],
                )
            else:
                train_xmin = min(train_xmin, geotransform[0])
                train_ymin = min(train_ymin, geotransform[3])
                train_xmax = max(train_xmax, geotransform[0])
                train_ymax = max(train_ymax, geotransform[3])
        return [train_xmin, train_ymin, train_xmax, train_ymax]

    def create_extent(self, path: Union[str, pathlib.Path]):
        if isinstance(path, str):
            path = pathlib.Path(path)

        train_db = polars.read_parquet(path / "train/metadata.parquet")
        validation_db = polars.read_parquet(path / "validation/metadata.parquet")
        test_db = polars.read_parquet(path / "test/metadata.parquet")

        # Get the extent of the dataset
        train_bbox = self.create_bbox(train_db)
        validation_bbox = self.create_bbox(validation_db)
        test_bbox = self.create_bbox(test_db)

        # Get the time interval of the dataset

        dates_start_train = train_db["start_datetime"].str.to_datetime(
            format="%Y-%m-%dT%H:%M:%S"
        )
        dates_start_val = validation_db["start_datetime"].str.to_datetime(
            format="%Y-%m-%dT%H:%M:%S"
        )
        dates_start_test = test_db["start_datetime"].str.to_datetime(
            format="%Y-%m-%dT%H:%M:%S"
        )

        self.extent = {
            "spatial": {"bbox": [train_bbox, validation_bbox, test_bbox]},
            "temporal": {
                "interval": [
                    [
                        min(dates_start_train).isoformat(),
                        max(dates_start_train).isoformat(),
                    ],
                    [
                        min(dates_start_val).isoformat(),
                        max(dates_start_val).isoformat(),
                    ],
                    [
                        min(dates_start_test).isoformat(),
                        max(dates_start_test).isoformat(),
                    ],
                ]
            },
        }

    def create_jsonfile(self, path: Union[str, pathlib.Path]):
        if isinstance(path, str):
            path = pathlib.Path(path)

        # save the collection
        with open(path / "main.json", "w") as f:
            json_file = self.model_dump()
            json_file = {k.replace("ml_", "ml:"): v for k, v in json_file.items()}
            json_file = {
                k: json_file[k]
                for k in sorted(json_file, key=lambda x: (x.startswith("ml:"), x))
            }
            json.dump(json_file, f, indent=4)

        return None

    def create_parquet(
        self,
        path: Union[str, pathlib.Path],
        checksum: bool = True,
        num_workers: int = 0,
        verbose: bool = False
    ):
        if isinstance(path, str):
            path = pathlib.Path(path)

        create_parquet(
            path=path,
            checksum=checksum,
            num_workers=num_workers,
            verbose=verbose
        )        

    def add_image(self, img: Union[str, pathlib.Path], path: Union[str, pathlib.Path]):
        if isinstance(path, str):
            path = pathlib.Path(path)
        img_suffix = pathlib.Path(img).suffix
        # is a path?
        if pathlib.Path(img).exists():
            img = str(pathlib.Path(img).absolute())
            outimg = path / "header.png"
            shutil.copyfile(img, outimg)
        elif validators.url(img):
            outimg = path / "header.png"
            with requests.get(img, stream=True) as r:
                r.raise_for_status()
                img = r.raw
                with open(path / ("header" + img_suffix), "wb") as f:
                    f.write(r.content)
        return None

    def add_documentation(self, path: Union[str, pathlib.Path]):
        if isinstance(path, str):
            path = pathlib.Path(path)
        mdFile = MdUtils(file_name=path / "README.md")

        # Create yaml header ------------------------------------
        mdFile.new_line("---")
        mdFile.new_line(f"language:")
        mdFile.new_line(f"- en")
        if self.keywords is not None:
            mdFile.new_line(f"tags:")
            for tag in self.keywords:
                mdFile.new_line(f"  - {tag}")
        mdFile.new_line(f"pretty_name: {self.id}")
        mdFile.new_line("---")

        # Set title, subtitle and description --------------------
        mdFile.new_header(level=1, title=f"{self.id}")
        if self.title is not None:
            mdFile.new_line(f"{self.title}", bold_italics_code="cib")
        mdFile.new_paragraph(f"{self.description}\n")
        mdFile.new_paragraph(f"ML-STAC Snippet", bold_italics_code="b")

        # Add code snippet ---------------------------------------
        url = (
            self.ml_train.link[: self.ml_train.link.strip("/").rfind("/")]
            + "/main.json"
        )
        mdFile.new_line("```python")
        mdFile.new_line(f"import mlstac\nsecret = '{url}'")
        mdFile.new_line(
            f"train_db = mlstac.load(secret, framework='torch', stream=True, device='cpu')"
        )
        mdFile.new_line("```")

        # Add image ----------------------------------------------
        if pathlib.Path.exists(path / "header.png"):
            img_head = Html.image(path="header.png", align="center")
            mdFile.new_paragraph(img_head)
        elif pathlib.Path.exists(path / "header.jpg"):
            img_head = Html.image(path="header.jpg", align="center")
            mdFile.new_paragraph(img_head)

        # Add data raw repository --------------------------------
        if self.ml_spectral is not None:
            mdFile.new_paragraph(
                "Sensor: " + self.ml_spectral.sensor, bold_italics_code="b"
            )
        
        mdFile.new_paragraph(
            "ML-STAC Task: " + ", ".join(self.ml_task), bold_italics_code="b"
        )

        if self.ml_raw_data_url is not None:
            mdFile.new_paragraph(
                f"Data raw repository:  "
                + mdFile.new_inline_link(link=self.ml_raw_data_url),
                bold_italics_code="b",
            )

        if self.ml_discussion_url is not None:
            mdFile.new_paragraph(
                f"Dataset discussion:  "
                + mdFile.new_inline_link(link=self.ml_discussion_url),
                bold_italics_code="b",
            )
        
        if self.ml_reviewers is not None:
            mdFile.new_paragraph(
                f"Review mean score:  {self.get_review_mean_score()}", bold_italics_code="b"
            )

        if self.ml_split_strategy is not None:
            mdFile.new_paragraph(
                f"Split_strategy:  " + self.ml_split_strategy, bold_italics_code="b"
            )

        if self.ml_paper is not None:
            mdFile.new_paragraph(
                f"Paper:  " + mdFile.new_inline_link(link=self.ml_paper),
                bold_italics_code="b",
            )

        # Add Provider --------------------------------------------
        mdFile.new_header(level=2, title=f"Data Providers")
        list_of_strings = ["Name", "Role", "URL"]
        for p in self.providers:
            list_of_strings.extend([p["name"], p["roles"], p["url"]])
        mdFile.new_table(
            columns=3,
            rows=len(self.providers) + 1,
            text=list_of_strings,
            text_align="center",
        )

        # Add Authors ---------------------------------------------
        # if len(self.ml_authors.authors) > 0:
        #    mdFile.new_header(level=2, title=f"Authors")
        #    list_of_strings = ["Name", "Organization"]
        #    for p in self.ml_authors:
        #        list_of_strings.extend([p['name'], p['organization']])
        # mdFile.new_table(columns=2, rows=len(self.ml_authors.authors)+1, text=list_of_strings, text_align='center')

        # Add Curators --------------------------------------------
        if self.ml_curators is not None:
            mdFile.new_header(level=2, title=f"Curators")
            list_of_strings = ["Name", "Organization", "URL"]
            for p in self.ml_curators.curators:
                list_of_strings.extend([p.name, p.organization, p.links[0].href])
            mdFile.new_table(
                columns=3,
                rows=len(self.ml_curators.curators) + 1,
                text=list_of_strings,
                text_align="center",
            )

        # Add Reviewers --------------------------------------------
        if self.ml_reviewers is not None:
            mdFile.new_header(level=2, title=f"Reviewers")
            list_of_strings = ["Name", "Organization", "URL", "Score"]
            for reviewer in self.ml_reviewers.reviewers:
                p = reviewer.reviewer
                s = reviewer.score
                list_of_strings.extend([p.name, p.organization, p.links[0].href, s])
            mdFile.new_table(
                columns=4,
                rows=len(self.ml_reviewers.reviewers) + 1,
                text=list_of_strings,
                text_align="center",
            )

        # Add Labels ----------------------------------------------
        if self.ml_labels is not None:
            mdFile.new_header(level=2, title="Labels")
            list_of_strings = ["Name", "Value"]
            for k, v in self.ml_labels.labels.items():
                list_of_strings.extend([k, v])
            mdFile.new_table(
                columns=2,
                rows=len(self.ml_labels.labels) + 1,
                text=list_of_strings,
                text_align="center",
            )

        # Add Dimensions ------------------------------------------
        if self.ml_dimensions is not None:
            mdFile.new_header(level=2, title=f"Dimensions")
            for k, v in self.ml_dimensions.model_dump().items():
                if len(v["dimensions"]) > 0:
                    mdFile.new_header(level=3, title=f"{k}")
                    list_of_strings = ["Axis", "Name", "Description"]
                    for p in v["dimensions"]:
                        list_of_strings.extend([p["axis"], p["name"], p["description"]])
                    mdFile.new_table(
                        columns=3,
                        rows=len(v["dimensions"]) + 1,
                        text=list_of_strings,
                        text_align="center",
                    )

        # Add Spectral Bands --------------------------------------
        if self.ml_spectral is not None:
            mdFile.new_header(level=2, title=f"Spectral Bands")
            list_of_strings = [
                "Name",
                "Common Name",
                "Description",
                "Center Wavelength",
                "Full Width Half Max",
                "Index",
            ]
            for p in self.ml_spectral.bands:
                list_of_strings.extend(
                    [
                        p.name,
                        p.common_name,
                        p.description,
                        p.center_wavelength,
                        p.full_width_half_max,
                        p.index,
                    ]
                )
            mdFile.new_table(
                columns=6,
                rows=len(self.ml_spectral.bands) + 1,
                text=list_of_strings,
                text_align="center",
            )

        file = mdFile.get_md_text().replace("\n\n\n  \n", "").replace("  \n", "\n")
        with open(path / "README.md", "w") as f:
            f.write(file)
