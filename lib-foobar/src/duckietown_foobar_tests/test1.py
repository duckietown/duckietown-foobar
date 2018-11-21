# coding=utf-8
import numpy as np
from comptests import comptest, run_module_tests, comptest_fails


@comptest
def test_sum1():
    print('trying to check fp math')
    assert 0.1 + 0.2 != 0.3


@comptest
def test_sum2():
    np.testing.assert_almost_equal(0.1 + 0.2, 0.3)

@comptest
def test_to_fail():
    assert 2 == 1

# use comptest_fails for a test that is supposed to fail
@comptest_fails
def test_supposed_to_fail():
    raise Exception()


if __name__ == '__main__':
    run_module_tests()
