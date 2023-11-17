use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;
extern crate filon as filon_rs;

#[pyfunction]
fn filon_tab_sin(ftab: Vec<f64>, a: f64, b: f64, sin_coeff: f64) -> PyResult<f64> {
    match filon_rs::filon_tab_sin(ftab, a, b, sin_coeff) {
        Ok(result) => Ok(result),
        Err(error) => Err(PyValueError::new_err(error.to_string()))
    }
}

#[pyfunction]
fn filon_tab_cos(ftab: Vec<f64>, a: f64, b: f64, cos_coeff: f64) -> PyResult<f64> {
    match filon_rs::filon_tab_cos(ftab, a, b, cos_coeff) {
        Ok(result) => Ok(result),
        Err(error) => Err(PyValueError::new_err(error.to_string()))
    }
}


/// A Python module implemented in Rust.
#[pymodule]
fn pyfilon(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(filon_tab_sin, m)?)?;
    m.add_function(wrap_pyfunction!(filon_tab_cos, m)?)?;
    Ok(())
}
