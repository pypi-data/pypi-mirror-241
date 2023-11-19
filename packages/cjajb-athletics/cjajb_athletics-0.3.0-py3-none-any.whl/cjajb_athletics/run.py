"""
The module computes the points for a run discipline.

Cyrille Polier 2023
"""

import numpy as np


def _fsa_2010(
    performance: float | str | np.ndarray, _a: float, _b: float, _c: float
) -> int | np.ndarray:
    """Compute the points using the FSA 2010 table.

    Parameters for the formula can be found on the Swiss Athletics website:
    https://swiss-athletics.ch/fr/baremes/
    https://swiss-athletics.ch/de/wertungstabellen/

    Args:
        performance (float | str | np.ndarray): The performance in seconds for an athlete or an array of performances.
        _a (float): The a parameter for the formula given in the FSA 2010 table.
        _b (float): The b parameter for the formula given in the FSA 2010 table.
        _c (float): The c parameter for the formula given in the FSA 2010 table.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """

    if isinstance(performance, np.ndarray):
        points = _a * np.power((_b - 100 * performance) / 100, _c, dtype=complex)
        points = np.where(np.iscomplex(points), 0, points)
        return np.minimum(np.floor(points.real), 1200)

    if isinstance(performance, str):
        performance = float(performance)

    point = _a * ((_b - 100 * performance) / 100) ** _c
    point = 0 if isinstance(point, complex) else point
    return np.minimum(np.floor(point), 1200)


# Men tables
def flat_50_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 50m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 8.05569, 1300, 2.5)


def flat_60_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 60m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 6.30895, 1460, 2.5)


def flat_80_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 80m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 3.80423, 1820, 2.5)


def flat_100_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 100m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 7.080303, 2150, 2.1)


def flat_200_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 200m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 1.31532, 4567, 2.1)


def flat_300_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 300m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.492671, 7295, 2.1)


def flat_400_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 400m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.249724, 10082, 2.1)


def flat_600_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 600m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.086375, 16833, 2.1)


def flat_800_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 800m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.042083, 23537, 2.1)


def flat_1000_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 1000m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.0068251, 32581, 2.3)


def flat_1500_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 1500m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.0024384, 50965, 2.3)


def flat_2000_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 2000m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.0011358, 71036, 2.3)


def flat_3000_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 3000m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.00041504, 110024, 2.3)


def flat_5000_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 5000m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.00011812, 189996, 2.3)


def flat_10000_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 10000m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.000021844, 395879, 2.3)


def hurdles_50_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 50m hurdles for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 14.460128, 1459, 2.1)


def hurdles_60_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 60m hurdles for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 10.294837, 1715, 2.1)


def hurdles_80_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 80m hurdles for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 5.925928, 2231, 2.1)


def hurdles_100_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 100m hurdles for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 3.82844, 2747, 2.1)


def hurdles_110_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 110m hurdles for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 3.174673, 3003, 2.1)


def hurdles_300_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 300m hurdles for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.364731, 8190, 2.1)


def hurdles_400_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 400m hurdles for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.211237, 10921, 2.1)


def st_1500_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 1500m steeplechase for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.0018664, 56163, 2.3)


def st_2000_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 2000m steeplechase for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.00094366, 77009, 2.3)


def st_3000_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 3000m steeplechase for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.00035433, 117893, 2.3)


def relay_4_x_100_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 4x100m men relay.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.355982, 8600, 2.1)


def relay_4_x_400_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 4x400m men relay.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.013902, 40328, 2.1)


# Women tables
def flat_50_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 50m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 9.42366, 1300, 2.5)


def flat_60_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 60m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 7.48676, 1460, 2.5)


def flat_80_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 80m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 4.22443, 1850, 2.5)


def flat_100_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 100m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 7.89305, 2180, 2.1)


def flat_200_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 200m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 1.435839, 4649, 2.1)


def flat_300_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 300m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.515644, 7564, 2.1)


def flat_400_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 400m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.261208, 10454, 2.1)


def flat_600_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 600m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.089752, 17543, 2.1)


def flat_800_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 800m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.04362, 24531, 2.1)


def flat_1000_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 1000m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.006914, 34158, 2.3)


def flat_1500_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 1500m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.0024951, 53216, 2.3)


def flat_2000_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 2000m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.0011486, 74565, 2.3)


def flat_3000_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 3000m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.00042789, 114561, 2.3)


def flat_5000_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 5000m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.00011545, 202413, 2.3)


def flat_10000_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 10000m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.000021257, 422397, 2.3)


def hurdles_50_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 50m hurdles for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 16.638377, 1448, 2.1)


def hurdles_60_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 60m hurdles for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 12.060698, 1688, 2.1)


def hurdles_80_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 80m hurdles for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 7.107482, 2171, 2.1)


def hurdles_100_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 100m hurdles for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 4.674232, 2650, 2.1)


def hurdles_300_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 300m hurdles for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.371294, 8570, 2.1)


def hurdles_400_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 400m hurdles for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.217291, 11424, 2.1)


def st_1500_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 1500m steeplechase for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.0020583, 58137, 2.3)


def st_2000_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 2000m steeplechase for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.0009372, 81460, 2.3)


def st_3000_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 3000m steeplechase for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.00034914, 125154, 2.3)


def relay_4_x_100_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 4x100m women relay.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.405548, 8720, 2.1)


def relay_4_x_400_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 4x400m women relay.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 0.014782, 41816, 2.1)
