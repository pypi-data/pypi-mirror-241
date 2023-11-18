"""Setup for azuresphere_imagemetadata."""
#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import find_packages, setup

NAME = "azuresphere_imagemetadata"
VERSION = "0.0.4"


# The full list of classifiers is available at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

DEPENDENCIES = [
    "cryptography >= 41.0.2",
]

setup(
    name=NAME,
    version=VERSION,
    description="A library for parsing and composing image metadata for azure sphere devices",
    license="MIT",
    author="Microsoft Corporation",
    author_email="azspheremfrsamplesup@microsoft.com",
    url="https://learn.microsoft.com/azure-sphere/",
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=["tests*"]),
    python_requires=">=3.8",
    install_requires=DEPENDENCIES,
    package_data={"azuresphere_imagemetadata": ["certificates/*"]},
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
)
