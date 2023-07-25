#!/usr/bin/env python

# This has only been added to allow editable dev installs, pyproject.toml replaces setup.py
# e.g. pip install -e .

import setuptools

def get_description():
    # Read description from README.md
    with open("README.md", "r") as f:
        return f.read()

if __name__ == "__main__":
    setuptools.setup(
        description=get_description(),
        long_description_content_type="text/markdown",
    )
