"""
This module contains the technical discipline formula collection.
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
        points = _a * np.power((100 * performance - _b) / 100, _c, dtype=complex)
        points = np.where(np.iscomplex(points), 0, points)
        return np.minimum(np.floor(points.real), 1200)
    if isinstance(performance, str):
        performance = float(performance)
    point = _a * ((100 * performance - _b) / 100) ** _c
    point = 0 if isinstance(point, complex) else point
    return np.minimum(np.floor(point), 1200)


# Men tables
def high_jump_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the high jump men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 732.15375, 75, 1)


def pole_vault_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the pole vault men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 234.78771, 80, 1)


def long_jump_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the long jump men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 136.08157, 130, 1.1)


def triple_jump_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the triple jump men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 86.950221, 395, 1)


def shot_put_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the shot put men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 82.491673, 178, 0.9)


def discus_throw_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the discus throw men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 28.891406, 494, 0.9)


def hammer_throw_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the hammer throw men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 24.978132, 581, 0.9)


def javelin_throw_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the javelin throw men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 23.247477, 602, 0.9)


def ball_throw_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the ball throw men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 19.191528, 600, 0.9)


# Women tables
def high_jump_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the high jump women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 942.65514, 75, 1)


def pole_vault_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the pole vault women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 303.79747, 80, 1)


def long_jump_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the long jump women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 171.91361, 125, 1.1)


def triple_jump_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the triple jump women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 106.044538, 374, 1)


def shot_put_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the shot put women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 83.435373, 130, 0.9)


def discus_throw_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the discus throw women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 27.928062, 362, 0.9)


def hammer_throw_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the hammer throw women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 25.267696, 405, 0.9)


def javelin_throw_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the javelin throw women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 28.058125, 360, 0.9)


def ball_throw_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the ball throw women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 24.63917, 500, 0.9)
