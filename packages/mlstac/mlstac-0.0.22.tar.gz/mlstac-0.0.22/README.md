#  

<p align="center">
  <img src="./mlstac/assets/img/banner.png" width="100%">
</p>

<p align="center">
    <em>A Common Language for EO Machine Learning Data</em>
</p>
<p align="center">
<a href='https://pypi.python.org/pypi/mlstac'>
    <img src='https://img.shields.io/pypi/v/mlstac.svg' alt='PyPI' />
</a>
<a href='https://anaconda.org/conda-forge/mlstac'>
    <img src='https://img.shields.io/conda/vn/conda-forge/mlstac.svg' alt='conda-forge' />
</a>
<a href='https://mlstac.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/mlstac/badge/?version=latest' alt='Documentation Status' />
</a>
<a href="https://opensource.org/licenses/MIT" target="_blank">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
</a>
<a href="https://github.com/psf/black" target="_blank">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Black">
</a>
<a href="https://pycqa.github.io/isort/" target="_blank">
    <img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336" alt="isort">
</a>
</p>

---

**GitHub**: [https://github.com/IPL-UV/ML-STAC](https://github.com/IPL-UV/ML-STAC)

**Documentation**: [https://mlstac.readthedocs.io/](https://mlstac.readthedocs.io/)

**PyPI**: [https://pypi.org/project/mlstac/](https://pypi.org/project/mlstac/)

**Conda-forge**: [https://anaconda.org/conda-forge/mlstac](https://anaconda.org/conda-forge/mlstac)

**Tutorials**: [https://mlstac.readthedocs.io/en/latest/tutorials.html](https://mlstac.readthedocs.io/en/latest/tutorials.html)

---

<i>
<font color="red">Explicit is better than implicit.</font><br>
<font color="green">Flat is better than nested.</font><br>
<font color="blue">Optimized storage saves more than just space.</font><br>
<font color="purple">Special cases aren't special enough to break the rules.</font><br>
<font color="orange">Dive directly into analysis, data always must be on demand</font><br>
</i>

## **Overview** 📜

**ML-STAC** provides a unified structure for cataloguing, describing, and adapting Earth Observation (EO) datasets into a format optimised for training Machine Learning (ML) models. Check the simple usage of `mlstac` here:

```python
import mlstac

# Create a Dataset using the ML-STAC specification
json_file = "https://huggingface.co/datasets/jfloresf/demo/raw/main/main.json"
train_db = mlstac.load(json_file, framework="torch", stream=False, device="cpu")
print(train_db[4])

# {'input': tensor([[[ 6.3199,  6.3629,  6.4148,  ..., 10.4104, 10.5109, 10.3847],
#           [ 6.3850,  6.3615,  6.4166,  ..., 10.4540, 10.4384, 10.4554],
#           [ 6.3519,  6.3176,  6.3575,  ..., 10.4247, 10.4618, 10.4257]]]),
#  'target': tensor([[[ 6.3199,  6.3629,  6.4148,  ..., 10.4104, 10.5109, 10.3847],
#           [ 6.3850,  6.3615,  6.4166,  ..., 10.4540, 10.4384, 10.4554],
#           [ 6.3519,  6.3176,  6.3575,  ..., 10.4247, 10.4618, 10.4257]]])
# }
```

**ML-STAC** is strongly influenced by the [STAC](https://stacspec.org/en) specification and its extensions, [single-file-stac](https://github.com/stac-extensions/single-file-stac) (Deprecated), [TrainingDML-AI](https://github.com/TrainingDML/trainingdml-ai-extension/tree/main) and [ML AOI](https://github.com/stac-extensions/ml-aoi#ml-aoi-extension). Additionally, we have incorporated naming conventions as discussed in the [OGC Training Data Markup Language - AI Conceptual Model Standard](https://github.com/opengeospatial/TrainingDML-AI_SWG).

## **Is ML-STAC an STAC Extension?** 🤔

Within the ML-STAC specification, each dataset is treated as an [STAC Collection](https://github.com/radiantearth/stac-spec/blob/master/collection-spec/collection-spec.md). Learn more at [STAC-ML](https://github.com/IPL-UV/ML-STAC/tree/main/mlstac/collection). However, each sample or element within that dataset is not considered an [STAC Item](https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md). Instead, we propose a new data structure called [ML-STAC Sample](https://github.com/IPL-UV/ML-STAC/tree/main/mlstac/sample), which is optimized for efficient read access to a wide range of data types, including images, text, and video.

## **The ML-STAC specification** 📋

The ML-STAC Specification consists of 2 interrelated specifications.

<img align="right" width="50%" src="./mlstac/assets/img/structure.png">

- **[ML-STAC Sample](./mlstac/sample/specification.md)** is the core atomic unit, representing a single data sample as [safetensor](https://github.com/huggingface/safetensors) file.

-  **[ML-STAC Collection](./mlstac/collection/specification.md)**, is an extension for STAC Collections that aggregates information about ML tasks, licenses, providers, and more. Each ML-STAC Collection must contain three [Catalog](./mlstac/catalog/README.md) objects: train, validation, and test.

Additionally, the ML-STAC specification includes an [API](./mlstac/api/README.md) interface, giving users on-demand access to datasets that 
conform to the ML-STAC specification.

## **How can I adapt my dataset to align with the ML-STAC specification?** 🔧

The process is straightforward for the vast majority of EO ML datasets. Here are the typical steps we follow.

1. Check to which [ML Task]() your dataset fixes better, we currently support more than 10 different tasks including multi-modal cases.
2. Create a generic dataloader (iterator object) using your favourite framework.
3. Use the [ml-stac toolbox]() and the iterator object (from step 2) to create [safetensors]() easily.
4. Move your dataset to your favourite file storage system (e.g. Local, AWS S3, Hugging Face Datasets, Azure Blob Storage, etc.).
5. Create a ML-STAC Collection object. We highly recommend you use `mlstac.collection.datamodel` validators.
6. Success! Remember that `mlstac` is multi-framework, so you can load your dataset in your favourite framework
   without needing additional dependencies (we currently support `torch`, `tensorflow`, `paddle`, `jax` and `numpy`).

## **Installation** 🚀

Install the latest version from PyPI:

```
pip install mlstac
```

Upgrade `mlstac` by running:

```
pip install -U mlstac
```

Install the latest version from conda-forge:

```
conda install -c conda-forge mlstac
```

Install the latest dev version from GitHub by running:

```
pip install git+https://github.com/ipl-uv/mlstac
```

## **Contributing** 🤝

We welcome and encourage anyone interested in improving or expanding the ML-STAC specification to join our collaborative efforts. Before becoming a part of our community, kindly familiarize yourself with our [contribution guidelines](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md). 

## **License** 🛡️

The project is licensed under the GNU General Public License v3.0.

## **Acknowledgment** 📖

This project has been made possible thanks to the collaboration between 5 research groups: Image & Signal Processing (ISP), the Remote Sensing Centre for Earth System Research (RSC4Earth), the Information Technologies for the Intelligent Digitization of Objects and Processes (TIDOP), the High Mountain Ecosystem (EcoHydro), and the Ecotoxicology Laboratory (EcoLab). We received funding from the National Council of Science, Technology, and Technological Innovation (CONCYTEC, Peru) under the “Proyectos de Investigación Básica – 2023-01” program (PE501083135-2023-PROCIENCIA).

<p align="center">
  <img src="./mlstac/assets/img/institutions.png" width=70%>
</p>
