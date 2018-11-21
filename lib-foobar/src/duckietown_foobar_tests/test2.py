# coding=utf-8
from comptests import comptest, run_module_tests

from duckietown_foobar import FoobarAlgo

@comptest
def test_foo():

    c = FoobarAlgo(param1=1)
    c.doit(10)


if __name__ == '__main__':
    run_module_tests()
