import io
import os
import re

from setuptools import find_packages, setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


setup(
    name="mlstac",
    version="0.0.22",
    url="https://github.com/IPL-UV/ml-stac",
    license="GNU GPLv3",
    author="Cesar Aybar, Julio Contreras",
    author_email="cesar.aybar@uv.es, julio.contreras1@unmsm.edu.pe",
    description="A Common Language for Machine Learning Data",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    # remove all the example.py
    package_data={"mlstac": ["*example.py"]},
    install_requires=[
        "pydantic>=2.4.2",
        "polars>=0.19.12",
        "safetensors",        
        "validators",
        "requests",
        "mdutils",
        "torch",
        "tqdm",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
