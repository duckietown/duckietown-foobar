[![CircleCI](https://circleci.com/gh/duckietown/duckietown-foobar.svg?style=shield)](https://circleci.com/gh/duckietown/duckietown-foobar)

[![Coverage Status](https://coveralls.io/repos/github/duckietown/duckietown-foobar/badge.svg?branch=master18)](https://coveralls.io/github/duckietown/duckietown-foobar?branch=master18)

[![PyPI status](https://img.shields.io/pypi/status/duckietown_foobar.svg)](https://pypi.python.org/pypi/duckietown_foobar/)


[![PyPI pyversions](https://img.shields.io/pypi/pyversions/duckietown_foobar.svg)](https://pypi.python.org/pypi/duckietown_foobar/)


# Foobar library

A short description of the foobar library


## Installation from source

This is the way to install within a virtual environment created by 
using `pipenv`:

    $ pipenv install
    $ pipenv shell
    $ cd lib-foobar
    $ pip install -r requirements.txt
    $ python setup.py develop --no-deps
    
   
## Unit tests

Run this:

    $ make -C lib-foobar tests-clean tests
    
The output is generated in the folder in `lib-foobar/out-comptests/`.
