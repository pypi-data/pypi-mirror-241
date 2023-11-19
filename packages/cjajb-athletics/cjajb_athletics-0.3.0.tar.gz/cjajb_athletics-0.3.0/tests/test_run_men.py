"""Test all the running formulas for men
"""

import src.cjajb_athletics.run as Run


def test_50m():
    assert Run.flat_50_men(7.39) == 600


def test_60m():
    assert Run.flat_60_men(8.41) == 601


def test_80m():
    assert Run.flat_80_men(10.62) == 601


def test_100m():
    assert Run.flat_100_men(13.21) == 601


def test_200m():
    assert Run.flat_200_men(27.20) == 600


def test_300m():
    assert Run.flat_300_men(43.48) == 600


def test_400m():
    assert Run.flat_400_men(60.09) == 600


def test_600m():
    assert Run.flat_600_men(100.81) == 600


def test_800m():
    assert Run.flat_800_men(140.28) == 600


def test_1000m():
    assert Run.flat_1000_men(184.69) == 600


def test_1500m():
    assert Run.flat_1500_men(288.88) == 600


def test_2000m():
    assert Run.flat_2000_men(402.61) == 600


def test_3000m():
    assert Run.flat_3000_men(623.49) == 600


def test_5000m():
    assert Run.flat_5000_men(1076.62) == 600


def test_10000m():
    assert Run.flat_10000_men(2243.77) == 600


def test_50m_hurdles():
    assert Run.hurdles_50_men(8.69) == 601


def test_60m_hurdles():
    assert Run.hurdles_60_men(10.22) == 600


def test_80m_hurdles():
    assert Run.hurdles_80_men(13.29) == 600


def test_100m_hurdles():
    assert Run.hurdles_100_men(16.37) == 600


def test_110m_hurdles():
    assert Run.hurdles_110_men(17.89) == 600


def test_300m_hurdles():
    assert Run.hurdles_300_men(47.89) == 600


def test_400m_hurdles():
    assert Run.hurdles_400_men(65.10) == 600


def test_1500m_steeplechase():
    assert Run.st_1500_men(313.65) == 600


def test_2000m_steeplechase():
    assert Run.st_2000_men(436.51) == 600


def test_3000m_steeplechase():
    assert Run.st_3000_men(668.24) == 600


def test_4_x_100m_relay():
    assert Run.relay_4_x_100_men(51.60) == 600


def test_4_x_400m_relay():
    assert Run.relay_4_x_400_men(242.14) == 600
