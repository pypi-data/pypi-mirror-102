#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepmediation",
    version="0.0.1",
    author="Tanmay Nath",
    author_email="tnath3@jhu.edu",
    description="Deep-mediation: a new approach towards high-dimensional mediation analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meet10may/deepmediation",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ),
    
)
