"""Tests the Filon quadrature algorithm."""

from pyfilon import filon_fun_sin, filon_fun_cos, filon_fun_iexp

import numpy as np
import pytest


def identity(val):
    return val


def quadratic(val):
    return val**2 + 3 * val + 7


def log(val):
    return np.log(1 + val)


def piecewise(val):
    if val < np.pi:
        return val
    else:
        return val + 1 / 2


def pi_sin(val):
    return np.sin(np.pi * val)


@pytest.mark.parametrize('points', [161, 321, 641])
@pytest.mark.parametrize(
    'function, exact',
    [
        (identity, (-np.pi / 5)),
        (quadratic, ((-3 * np.pi - 2 * np.pi**2) / 5)),
        (log, (-0.1961185699426520514276893141271915)),
        (piecewise, (-np.pi / 5)),
        (pi_sin, (10 * np.sin(2 * (np.pi**2)) / (np.pi**2 - 100))),
    ],
)
def test_filon_sin_points(points, function, exact):
    """Tests the accuracy of filon_fun_sin over varying mesh sizes."""
    actual = filon_fun_sin(function, 0, 2 * np.pi, 10, points)
    np.testing.assert_allclose(actual, exact, rtol=1e-2, atol=1e-2)

@pytest.mark.parametrize('points', [161, 321, 641])
@pytest.mark.parametrize(
    'function, exact',
    [
        (identity, 0),
        (quadratic, (np.pi/25)),
        (log, (-0.008140318405890393430327734)),
        (piecewise, 0),
        (pi_sin, (2*np.pi * np.sin((np.pi**2))**2 / (np.pi**2 - 100))),
    ],
)
def test_filon_cos_points(points, function, exact):
    """Tests the accuracy of filon_fun_cos over varying mesh sizes."""
    actual = filon_fun_cos(function, 0, 2 * np.pi, 10, points)
    np.testing.assert_allclose(actual, exact, rtol=1e-2, atol=1e-2)

@pytest.mark.parametrize('points', [161, 321, 641])
@pytest.mark.parametrize(
    'function, exact',
    [
        (identity, (-1j*np.pi / 5)),
        (quadratic, (np.pi/25) + 1j*((-3 * np.pi - 2 * np.pi**2) / 5)),
        (log, -0.00844659 - 0.197627j),
        (piecewise, (-1j*np.pi / 5)),
        (pi_sin, -0.012907844945847433672 -0.086192145774330529j),
    ],
)
def test_filon_iexp_points(points, function, exact):
    """Tests the accuracy of filon_fun_cos over varying mesh sizes."""
    actual = filon_fun_iexp(function, 0, 2 * np.pi, 10, points)
    np.testing.assert_allclose(actual, exact, rtol=1e-2, atol=1e-2)
