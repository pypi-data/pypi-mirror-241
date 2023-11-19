"""
Test the 100m functions in the cjajb_athletics package.
Extensive testing for all special cases.
"""

import numpy
import src.cjajb_athletics.technic as Technic


def test_1200_points_limit():
    assert Technic.long_jump_men(9.00) == 1200


def test_1199_points():
    assert Technic.long_jump_men(8.53) == 1199


def test_1_point():
    assert Technic.long_jump_men(1.32) == 1


def test_0_point_limit():
    assert Technic.long_jump_men(0.00) == 0


def test_int():
    assert Technic.long_jump_men(8) == 1102


def test_string():
    assert Technic.long_jump_men("8") == 1102


def test_array():
    assert numpy.array_equal(
        Technic.long_jump_men(numpy.array([8, 9.00, 1.32, 0.00, 8.53])),
        numpy.array([1102, 1200, 1, 0, 1199]),
    )
