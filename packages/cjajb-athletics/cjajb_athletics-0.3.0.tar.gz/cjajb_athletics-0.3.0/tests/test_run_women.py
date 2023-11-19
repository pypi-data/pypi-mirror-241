"""Test all the running formulas for women
"""
import src.cjajb_athletics.run as Run


def test_50m():
    assert Run.flat_50_women(7.73) == 600


def test_60m():
    assert Run.flat_60_women(8.82) == 601


def test_80m():
    assert Run.flat_80_women(11.23) == 602


def test_100m():
    assert Run.flat_100_women(13.93) == 600


def test_200m():
    assert Run.flat_200_women(28.78) == 600


def test_300m():
    assert Run.flat_300_women(46.80) == 600


def test_400m():
    assert Run.flat_400_women(64.67) == 600


def test_600m():
    assert Run.flat_600_women(109.13) == 600


def test_800m():
    assert Run.flat_800_women(151.83) == 600


def test_1000m():
    assert Run.flat_1000_women(201.25) == 600


def test_1500m():
    assert Run.flat_1500_women(313.58) == 600


def test_2000m():
    assert Run.flat_2000_women(439.39) == 600


def test_3000m():
    assert Run.flat_3000_women(675.14) == 600


def test_5000m():
    assert Run.flat_5000_women(1192.56) == 600


def test_10000m():
    assert Run.flat_10000_women(2488.51) == 600


def test_50m_hurdles():
    assert Run.hurdles_50_women(8.96) == 601


def test_60m_hurdles():
    assert Run.hurdles_60_women(10.45) == 600


def test_80m_hurdles():
    assert Run.hurdles_80_women(13.44) == 600


def test_100m_hurdles():
    assert Run.hurdles_100_women(16.40) == 600


def test_300m_hurdles():
    assert Run.hurdles_300_women(51.98) == 600


def test_400m_hurdles():
    assert Run.hurdles_400_women(70.72) == 600


def test_1500m_steeplechase():
    assert Run.st_1500_women(343.72) == 600


def test_2000m_steeplechase():
    assert Run.st_2000_women(480.03) == 600


def test_3000m_steeplechase():
    assert Run.st_3000_women(737.57) == 600


def test_4_x_100m_relay():
    assert Run.relay_4_x_100_women(54.87) == 600


def test_4_x_400m_relay():
    assert Run.relay_4_x_400_women(261.67) == 600
