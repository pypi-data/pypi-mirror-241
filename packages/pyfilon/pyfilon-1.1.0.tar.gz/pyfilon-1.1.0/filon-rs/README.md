# filon
Implementation of Filon quadrature in Rust and Python.

The Filon quadrature is a quadrature for highly oscillatory
integrals, such as $\int_a^b f(x) sin(mx)$ or $\int_a^b f(x) cos(mx)$.

This package implements the Filon quadrature algorithm in Rust as well as
Python via [`PyO3`](https://github.com/PyO3/pyo3) and [`maturin`](https://github.com/PyO3/maturin).

This code ports [John Burkardt's implementation of Filon quadrature](https://people.math.sc.edu/Burkardt/cpp_src/filon/filon.html),
based on Chase and Fosdick's algorithm in the ACM, [available on Netlib as TOMS 353](https://netlib.org/toms/index.html).
