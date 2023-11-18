[![PyPI version](https://badge.fury.io/py/mvdate.svg)](https://badge.fury.io/py/mvdate)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mvdate)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-456789.svg)](https://github.com/psf/flake8)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json))](https://github.com/astral-sh/ruff)
[![Downloads](https://static.pepy.tech/badge/mvdate)](https://pepy.tech/project/mvdate)
[![Downloads](https://static.pepy.tech/badge/mvdate/month)](https://pepy.tech/project/mvdate)
[![Downloads](https://static.pepy.tech/badge/mvdate/week)](https://pepy.tech/project/mvdate)
[![Donate](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/slackline/donate)

# mvdate

A Python package to search for files and move them to a directory structure based on date.

## Motivation

I keep my pictures in a hierarchical data structure of `YYYY/MM/DD` but that isn't how my camera stores them. I wanted
an easy way to copy/move files to this structure.

## Installation

`mvdate` is available from [PyPI](https://pypi.org) to install...

```bash
pip install mvdate
```

### Development

If you wish to try the development version you can install directly using `pip`...

```bash
pip install mvdate@git+https://gitlab.com/nshephard/mvdate.git@main
```

Or if you are likely to want to tinker you can clone the repository and install (although you may wish to fork and clone
that if you want to contribute).

```bash
git clone git@gitlab.com:nshephard/mvdate.git
cd mvdate
pip install .
```

## Usage

To search the current directory for files ending with `png` and move them to `~/pics/YYYY/MM/DD/`

```bash
mvdate --base ./ --destination ~/pics/ --ext png
```

For all options see the help

```bash
mvdate --help
```

## Contributing

If you want to contribute merge requests are more than welcome. Fork and clone the repository and install the
development and test dependencies.

```bash
mkvirtualenv mvdate # Or similar depending on your preferences
git clone git@gitlab.com:nshephard/mvdate.git
cd mvdate
pip install .[dev,tests]
pre-commit install
```

I use various tools to lint and test the package, mostly via [pre-commit](https://pre-commit.com). These include
[pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks), [black](https://github.com/psf/black),
[markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) and [ruff](https://docs.astral.sh/ruff/). By using
`pre-commit` locally any contributions should then pass the GitLab CI pipelines I have in place.

## Links
