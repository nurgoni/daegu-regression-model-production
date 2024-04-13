#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'daegu_regression'
DESCRIPTION = "packaging regression model for production"
URL = "-"
EMAIL = "afgoniannur@gmail.com"
AUTHOR = "Annur Afgoni"
REQUIRES_PYTHON = ">=3.6.0"

long_description = DESCRIPTION

# Load the package's VERSION file as a dictionary.
about = {}
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR / 'requirements'
PACKAGE_DIR = ROOT_DIR / 'daegu_regression'
with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version


# What packages are required for this module to be executed?
def list_reqs(fname="requirements.txt"):
    try:
        with open(REQUIREMENTS_DIR / fname) as fd:
            return fd.read().splitlines()
    except FileNotFoundError:
        return [
            "numpy>=1.21.0,<2.0.0",
            "pandas>=1.3.5,<2.1.1",
            "pydantic>=1.8.1,<2.0.0",
            "scikit-learn>=1.1.3,<2.0.0",
            "strictyaml>=1.3.2,<2.0.0",
            "ruamel.yaml>=0.16.12,<1.0.0",
            "feature-engine>=1.0.2,<1.6.0",  # breaking change in v1.6.0
            "joblib>=1.0.1,<2.0.0"
        ]

# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    package_data={"daegu_regression": ["VERSION"]},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license="BSD-3",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)