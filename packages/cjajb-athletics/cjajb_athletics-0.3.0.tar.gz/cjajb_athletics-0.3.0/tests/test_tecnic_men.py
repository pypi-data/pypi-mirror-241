"""Test all the technic tables for men
"""

import src.cjajb_athletics.technic as Technic


def test_high_jump():
    assert Technic.high_jump_men(1.57) == 600


def test_pole_vault():
    assert Technic.pole_vault_men(3.36) == 601


def test_long_jump():
    assert Technic.long_jump_men(5.16) == 601


def test_triple_jump():
    assert Technic.triple_jump_men(10.86) == 600


def test_shot_put():
    assert Technic.shot_put_men(10.85) == 600


def test_discus_throw():
    assert Technic.discus_throw_men(34.04) == 600


def test_hammer_throw():
    assert Technic.hammer_throw_men(40.01) == 600


def test_javelin_throw():
    assert Technic.javelin_throw_men(43.06) == 600


def test_ball_throw():
    assert Technic.ball_throw_men(51.84) == 600
