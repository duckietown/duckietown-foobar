
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
