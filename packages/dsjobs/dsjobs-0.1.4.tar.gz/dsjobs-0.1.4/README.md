# DesignSafe Jobs

[![build and test](https://github.com/DesignSafe-CI/dsjobs/actions/workflows/build-test.yml/badge.svg)](https://github.com/DesignSafe-CI/dsjobs/actions/workflows/build-test.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)
[![Docs](https://img.shields.io/badge/view-docs-8A2BE2?color=8A2BE2)](https://designsafe-ci.github.io/dsjobs/dsjobs/index.html)

`dsjobs` is a library that simplifies the process of submitting, running, and monitoring [TAPIS v2 / AgavePy](https://agavepy.readthedocs.io/en/latest/index.html) jobs on [DesignSafe](https://designsafe-ci.org) via [Jupyter Notebooks](https://jupyter.designsafe-ci.org).

## Features

* Simplified TAPIS v2 Calls: No need to fiddle with complex API requests. `dsjobs` abstracts away the complexities.

* Seamless Integration with DesignSafe Jupyter Notebooks: Launch DesignSafe applications directly from the Jupyter environment.

## Installation

Install `dsjobs` via pip

```shell
pip3 install dsjobs
```

To install the current development version of the library use:

```shell
pip install git+https://github.com/DesignSafe-CI/dsjobs.git --quiet
```

## Example usage:

* [Jupyter Notebook Templates](example-notebooks/template-mpm-run.ipynb) using DSJobs.

* View [DSJobs API doc](https://designsafe-ci.github.io/dsjobs/dsjobs/index.html)

On [DesignSafe Jupyter](https://jupyter.designsafe-ci.org/):

Install the latest version of `dsjobs` and restart the kernel (Kernel >> Restart Kernel):

```python
# Remove any previous installations
!pip uninstall dsjobs -y
# Install 
!pip install dsjobs --quiet
```

* Import `dsjobs` library
```python
import dsjobs as ds
```

* To list all functions in `dsjobs`
```python
dir(ds)
```

## Documentation

View [DSJobs API doc](https://designsafe-ci.github.io/dsjobs/dsjobs/index.html)

To generate API docs:

```
pdoc --html --output-dir docs dsjobs --force
```

## Support

For any questions, issues, or feedback submit an [issue](https://github.com/DesignSafe-CI/dsjobs/issues/new)

## Development

To develop or test the library locally. Install [Poetry](https://python-poetry.org/docs/#installation). In the current repository run the following commands

```shell
poetry shell
poetry install
poetry build
```

To run the unit test
```shell
poetry run pytest -v
```

## License

`dsjobs` is licensed under the [MIT License](LICENSE.md).

## Authors

* Prof. Pedro Arduino, University of Washington
* Krishna Kumar, University of Texas at Austin