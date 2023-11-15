# Package using pyproject.toml

## Creating the package files

    packaging_tutorial/
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── src/
    │   └── your_package_YOUR_USERNAME_HERE/
    │       ├── __init__.py
    │       └── example.py
    └── tests/

## Choosing a build backend

Tools like pip and build do not actually convert your sources into a distribution package (like a wheel); that job is performed by a build backend. 

The build backend determines how your project will specify its configuration, including metadata (information about the project, for example, the name and tags that are displayed on PyPI) and input files.

Build backends have different levels of functionality, such as whether they support building extension modules, and you should choose one that suits your needs and preferences.

1. Hatchling
2. setuptools
3. Flit
4. PDM

others that support the [project] table for metadata.
The pyproject.toml tells build frontend tools like pip and build which backend to use for your project.

## Generating distribution archives

    python3 -m pip install --upgrade build

    python3 -m build

## Uploading the distribution archives

    python3 -m pip install --upgrade twine
