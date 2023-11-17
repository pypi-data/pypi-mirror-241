"""Quadrature functions for Python callables."""
from typing import Callable

from numpy import linspace

from pyfilon.pyfilon import filon_tab_sin, filon_tab_cos

def filon_fun_sin(func: Callable, a: float, b: float, sin_coeff: float, mesh_size: int) -> float:
    ftab = [func(x) for x in linspace(a, b, mesh_size)]
    return filon_tab_sin(ftab, a, b, sin_coeff)

def filon_fun_cos(func: Callable, a: float, b: float, cos_coeff: float, mesh_size: int) -> float:
    ftab = [func(x) for x in linspace(a, b, mesh_size)]
    return filon_tab_cos(ftab, a, b, cos_coeff)