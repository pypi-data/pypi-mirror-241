"""
Quadrature functions for Python callables.
Adapted from FILON: https://people.math.sc.edu/Burkardt/cpp_src/filon/filon.html

    Reference:
    Stephen Chase, Lloyd Fosdick,
    An Algorithm for Filon Quadrature,
    Communications of the Association for Computing Machinery,
    Volume 12, Number 8, August 1969, pages 453-457.

    Stephen Chase, Lloyd Fosdick,
    Algorithm 353: Filon Quadrature,
    Communications of the Association for Computing Machinery,
    Volume 12, Number 8, August 1969, pages 457-458.

    Bo Einarsson,
    Algorithm 418: Calculation of Fourier Integrals,
    Communications of the ACM,
    Volume 15, Number 1, January 1972, pages 47-48.
"""
from typing import Callable

from numpy import linspace

from pyfilon.pyfilon import filon_tab_sin, filon_tab_cos

def filon_fun_sin(func: Callable, a: float, b: float, sin_coeff: float, mesh_size: int) -> float:
    """
    Filon quadrature rule for `func` multiplied by sin(mx) over an interval.

    Parameters
    ----------
    func: Callable, float -> float
        The function f(x) over which to integrate.
    interval: Tuple[float, float]
        The interval to integrate over.
    num_points: int
        The number of datapoints at which the function is evaluated, including the
        endpoints. Must be an odd integer greater than 1.
    sin_coeff: float
        The coefficient of the sine function in the integrand; `m` in 'sin(mx)'

    Returns
    -------
    float
        The quadrature estimate of the integral func(x)*sin(mx) over the interval given.
    """

    ftab = [func(x) for x in linspace(a, b, mesh_size)]
    return filon_tab_sin(ftab, a, b, sin_coeff)

def filon_fun_cos(func: Callable, a: float, b: float, cos_coeff: float, mesh_size: int) -> float:
    """
    Filon quadrature rule for `func` multiplied by cos(mx) over an interval.

    Parameters
    ----------
    func: Callable, float -> float
        The function f(x) over which to integrate.
    interval: Tuple[float, float]
        The interval to integrate over.
    num_points: int
        The number of datapoints at which the function is evaluated, including the
        endpoints. Must be an odd integer greater than 1.
    cos_coeff: float
        The coefficient of the sine function in the integrand; `m` in 'cos(mx)'

    Returns
    -------
    float
        The quadrature estimate of the integral func(x)*cos(mx) over the interval given.
    """
    ftab = [func(x) for x in linspace(a, b, mesh_size)]
    return filon_tab_cos(ftab, a, b, cos_coeff)

def filon_fun_iexp(func: Callable, a: float, b: float, exp_coeff: float, mesh_size: int) -> float:
    """
    Filon quadrature rule for `func` multiplied by exp(imx) over an interval.

    Parameters
    ----------
    func: Callable, float -> float
        The function f(x) over which to integrate.
    interval: Tuple[float, float]
        The interval to integrate over.
    num_points: int
        The number of datapoints at which the function is evaluated, including the
        endpoints. Must be an odd integer greater than 1.
    sin_coeff: float
        The coefficient of the sine function in the integrand; `m` in 'exp(imx)'

    Returns
    -------
    float
        The quadrature estimate of the integral func(x)*exp(imx) over the interval given.
    """

    ftab = [func(x) for x in linspace(a, b, mesh_size)]
    return filon_tab_cos(ftab, a, b, exp_coeff) + 1j*filon_tab_sin(ftab, a, b, exp_coeff)