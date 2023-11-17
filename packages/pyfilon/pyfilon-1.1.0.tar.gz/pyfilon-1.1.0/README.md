# filon
Implementation of Filon quadrature in Rust (as [filon](https://crates.io/crates/filon)) and Python (as [pyfilon](https://pypi.org/project/pyfilon))

[![crates.io](https://img.shields.io/crates/v/filon?logo=rust&style=flat-square)](https://crates.io/crates/filon)
[![PyPI](https://img.shields.io/pypi/v/pyfilon.svg?logo=python&style=flat-square)](https://pypi.org/project/pyfilon)


The Filon quadrature is a quadrature for highly oscillatory
integrals, such as $\int_a^b f(x) sin(mx)$ or $\int_a^b f(x) cos(mx)$.

This package implements the Filon quadrature algorithm in Rust as well as
Python via [`PyO3`](https://github.com/PyO3/pyo3) and [`maturin`](https://github.com/PyO3/maturin).

Supports:
In Rust: quadrature for discretised functions with $sin(mx)$ and $cos(mx)$
In Python: quadrature for discretised and non-discretised functions with $sin(mx)$, $cos(mx)$ and $exp(imx)$.

This code ports [John Burkardt's implementation of Filon quadrature](https://people.math.sc.edu/Burkardt/cpp_src/filon/filon.html),
based on Chase and Fosdick's algorithm in the ACM, [available on Netlib as TOMS 353](https://netlib.org/toms/index.html).
