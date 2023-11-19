"""Test all the technic tables for women
"""

import src.cjajb_athletics.technic as Technic


def test_high_jump():
    assert Technic.high_jump_women(1.39) == 603


def test_pole_vault():
    assert Technic.pole_vault_women(2.78) == 601


def test_long_jump():
    assert Technic.long_jump_women(4.37) == 601


def test_triple_jump():
    assert Technic.triple_jump_women(9.40) == 600


def test_shot_put():
    assert Technic.shot_put_women(10.26) == 600


def test_discus_throw():
    assert Technic.discus_throw_women(33.83) == 600


def test_hammer_throw():
    assert Technic.hammer_throw_women(37.82) == 600


def test_javelin_throw():
    assert Technic.javelin_throw_women(33.66) == 600


def test_ball_throw():
    assert Technic.ball_throw_women(39.73) == 600
