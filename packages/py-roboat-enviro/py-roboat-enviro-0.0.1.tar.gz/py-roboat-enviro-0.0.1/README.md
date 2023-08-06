# py-roboat-enviro

![Test](https://github.com/drewmee/py-roboat-enviro/workflows/Test/badge.svg)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/drewmee/py-roboat-enviro/blob/master/LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A python wrapper for the Roboat environmental data RESTful API

## Installation

Install via pip:

    $ pip install py_roboat_enviro [--upgrade]

## Documentation

  Full documentation can be found [here](https://py-roboat-enviro.readthedocs.io/).

## Dependencies for Local Development

If you wish to build the local documentation or run unit tests, there are a few additional dependencies. Those can be installed by:

pip install -e ".[docs, tests]"

## Building docs locally
make -C docs clean
make -C docs html

## Run tests locally
pytest tests/test_api.py -s

## License

This library is licensed under the MIT license. The full text of the license can be found in this repository at LICENSE.txt.