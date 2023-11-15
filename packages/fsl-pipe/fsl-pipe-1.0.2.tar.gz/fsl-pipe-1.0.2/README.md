[![Documentation](https://img.shields.io/badge/Documentation-fsl--pipe-blue)](https://open.win.ox.ac.uk/pages/fsl/fsl-pipe)
[![File-tree Documentation](https://img.shields.io/badge/Documentation-file--tree-blue)](https://open.win.ox.ac.uk/pages/fsl/file-tree)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6577069.svg)](https://doi.org/10.5281/zenodo.6577069)
[![Pipeline status](https://git.fmrib.ox.ac.uk/fsl/fsl-pipe/badges/main/pipeline.svg)](https://git.fmrib.ox.ac.uk/fsl/fsl-pipe/-/pipelines/latest)
[![Coverage report](https://git.fmrib.ox.ac.uk/fsl/fsl-pipe/badges/main/coverage.svg)](https://open.win.ox.ac.uk/pages/fsl/fsl-pipe/htmlcov)

Declative pipelines based on Filetrees. A pipeline is defined by:
- A file-tree, which defines the directory structure of the inputs and outputs of the pipeline. A tutorial on these file-trees is available [here](https://open.win.ox.ac.uk/pages/fsl/file-tree).
- A set of recipes describing how all the pipeline outputs are produced. A tutorial on writing these recipes is available [here](https://open.win.ox.ac.uk/pages/fsl/fsl-pipe).
Fsl-pipe will stitch these recipes together to produce any user-selected output files.
Resulting jobs will either run locally, run distributed using [dask](https://www.dask.org), or be submitted to a cluster using [fsl-sub](https://git.fmrib.ox.ac.uk/fsl/fsl_sub).

An example diffusion MRI pipeline using fsl-pipe with detailed comments is available [here](https://git.fmrib.ox.ac.uk/ndcn0236/fsl-pipe-example).

# Installation
```shell
pip install fsl-pipe
```

Any bug reports and feature requests are very welcome (see [issue tracker](https://git.fmrib.ox.ac.uk/fsl/fsl-pipe/-/issues)).

# Setting up local test environment
First clone the repository:
```shell
git clone https://git.fmrib.ox.ac.uk/fsl/fsl-pipe.git
```

Then, we install the package in an interactive manner:
```shell
cd fsl-pipe
pip install -e .
```

## Running tests
Tests are run using the [pytest](https://docs.pytest.org) framework. After installation (`pip install pytest`) they can be run from the project root as:
```shell
pytest src/tests
```

## Compiling documentation
The documentation is build using [sphinx](https://www.sphinx-doc.org/en/master/). After installation (`pip install sphinx`) run:
```shell
cd doc
sphinx-build source build
open build/index.html
```

## Contributing
[Merge requests](https://git.fmrib.ox.ac.uk/fsl/fsl-pipe/-/merge_requests) with any bug fixes or documentation updates are always welcome. 

For new features, please raise an [issue](https://git.fmrib.ox.ac.uk/fsl/fsl-pipe/-/issues) to allow for discussion before you spend the time implementing them.

## Releasing new versions
- Run `bump2version` (install using `pip install bump2version`)
- Push to gitlab (including tags in the push)
- After the continuous integration (CI) succeeds, manually run the job to upload fsl-pipe to pypi (see [here](https://git.fmrib.ox.ac.uk/fsl/fsl-pipe/-/pipelines/latest))
- Upload code on conda-forge using their automated release detection.
