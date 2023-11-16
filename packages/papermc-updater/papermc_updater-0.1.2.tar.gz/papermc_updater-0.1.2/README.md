# papermc-updater

[![GitHub version](https://badge.fury.io/gh/tjkessler%2Fpapermc-updater.svg)](https://badge.fury.io/gh/tjkessler%2Fpapermc-updater)
[![PyPI version](https://badge.fury.io/py/papermc-updater.svg)](https://badge.fury.io/py/papermc-updater)
[![GitHub license](https://img.shields.io/badge/license-Apache-blue.svg)](https://raw.githubusercontent.com/tjkessler/papermc-updater/master/LICENSE.txt)

A command-line tool to update a PaperMC server .jar file (in-place) to the latest build. Supports latest and previous MC versions.

## Installation

Requires Python 3.10+.

### From PyPI

```
$ python -m pip install papermc-updater
```

or

```
$ pip install papermc-updater
```

### From source

```
$ git clone https://github.com/tjkessler/papermc-updater
$ cd papermc-updater
$ python -m pip install .
```

## Usage

Warning: this tool replaces the existing PaperMC server .jar file!

### Command line

```
$ update-papermc $PATH_TO_EXISTING_JARFILE
```

The default MC version is `1.20.2` - specify a different MC version with:

```
$ update-papermc $PATH_TO_EXISTING_JARFILE --version 1.19.4
```

### Python script

```python
from papermc_updater import update_paper_to_latest

update_paper_to_latest("$PATH_TO_EXISTING_JARFILE", version="1.20.1")
```
