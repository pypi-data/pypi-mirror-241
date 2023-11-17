"""Setup for esrp-release-test."""
#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import find_packages, setup

NAME = "esrp-release-test"
VERSION = "27"


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
    "azure-storage-blob",
    "requests>=2.23.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="ESRP Release is a pathway to many abilities some consider to be, unnatural.",
    license="MIT",
    author="Microsoft Corporation",
    author_email="shmallip@microsoft.com",
    url="https://dev.azure.com/releaseado/MS.Ess.Release.VSTS.Extension/_git/esrp-release-test",
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=["tests*"]),
    python_requires=">=3.8",
    install_requires=DEPENDENCIES,
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
)
