# Package using pyproject.toml


1. The publisher is using the latest version of setuptools
2. The latest version of twine is used to upload the package
3. The user installing the package has at least Pip 9.0, or a client that supports the Metadata 1.2 specification.

## Creating the package files

    packaging_tutorial/
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── src/
    │   └── your_package/
    │       ├── __init__.py
    │       └── example.py
    └── tests/

## Dealing with the universal wheels

Traditionally, projects providing Python code that is semantically compatible with both Python 2 and Python 3, produce wheels that have a py2.py3 tag in their names.

It is often configured within setup.cfg under the [bdist_wheel] section by setting universal = 1 if they use setuptools.

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

## Defining the Python version required

    python3 -m pip install --upgrade setuptools twine

## Generating distribution archives

    python3 -m pip install --upgrade build

    python3 -m build

## Uploading the distribution archives

    python3 -m pip install --upgrade twine
    python3 -m twine upload --repository pypi dist/*

## Installing your newly uploaded package
    
    python3 -m pip install toml_package
    
