"""
Test the 100m functions in the cjajb_athletics package.
Extensive testing for all special cases.
"""

import numpy
import src.cjajb_athletics.run as Run


def test_100_men_1199():
    assert Run.flat_100_men(9.98) == 1199


def test_100_men_1():
    assert Run.flat_100_men(21.10) == 1


def test_100_women_1199():
    assert Run.flat_100_women(10.86) == 1199


def test_100_women_1():
    assert Run.flat_100_women(21.42) == 1


def test_100_men_over_1200():
    assert Run.flat_100_men(9.00) == 1200


def test_100_women_over_1200():
    assert Run.flat_100_women(9.00) == 1200


def test_100_men_under_0():
    assert Run.flat_100_men(22.00) == 0


def test_100_women_under_0():
    assert Run.flat_100_women(22.00) == 0


def test_100_men_int():
    assert Run.flat_100_men(10) == 1195


def test_100_women_int():
    assert Run.flat_100_women(11) == 1167


def test_100_men_string():
    assert Run.flat_100_men("10") == 1195


def test_100_women_string():
    assert Run.flat_100_women("11") == 1167


def test_100_men_array():
    assert numpy.array_equal(
        Run.flat_100_men(numpy.array([10, 9.98, 21.10, 9.00, 22.00, 30.0])),
        numpy.array([1195, 1199, 1, 1200, 0, 0]),
    )
