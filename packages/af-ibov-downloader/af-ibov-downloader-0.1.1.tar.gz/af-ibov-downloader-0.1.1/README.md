# Aerofin Ibov Downloader

A CLI that downloads archives from the ibovespa website.

## Requirements

* python >= 3.6
* asyncio
* typing (type hints)

## Installation

Intalling from gitlab:

```bash
pip install -u git+https://gitlab.com/aerofin/tooling/af-ibov-downloader.git@master
```

Installing from pypi:

```bash
pip install -u af-ibov-downloader
```

## Usage

Once installed, the CLi will be available as `af-ibov-downloader`.

Run `af-ibov-downloader --help` for commands or check the [docs website](https://af-ibov-archive.readthedocs.org).

## Development

A `Makefile` is provided for common tasks, such as running tests.

The project uses poetry ad "project tooling" but `requirements` files for both prod and dev are provided for convenience.

A `setup.py` file is generated using `dephell`.

Tests are based on `pytest` but they can be used by running `make test`.

The project also depends on `mypy` in strict mode which is used before running the actual tests.

## License

MIT
