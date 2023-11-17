use std::io::Error;
use std::io::ErrorKind;

/// FILON algorithms for oscillatory quadrature, adapted from John Burkardt:
/// https://people.math.sc.edu/Burkardt/cpp_src/filon/filon.cpp
//  Reference:
//
//    Milton Abramowitz, Irene Stegun,
//    Handbook of Mathematical Functions,
//    National Bureau of Standards, 1964,
//    ISBN: 0-486-61272-4,
//    LC: QA47.A34.
//
//    Stephen Chase, Lloyd Fosdick,
//    An Algorithm for Filon Quadrature,
//    Communications of the Association for Computing Machinery,
//    Volume 12, Number 8, August 1969, pages 453-457.
//
//    Stephen Chase, Lloyd Fosdick,
//    Algorithm 353:
//    Filon Quadrature,
//    Communications of the Association for Computing Machinery,
//    Volume 12, Number 8, August 1969, pages 457-458.
//
//    Philip Davis, Philip Rabinowitz,
//    Methods of Numerical Integration,
//    Second Edition,
//    Dover, 2007,
//    ISBN: 0486453391,
//    LC: QA299.3.D28.
//


/// estimates the integral of a function multiplied by sin(mx)
/// over the interval a, b.
///
///  Parameters:
///  ftab: Vec<f64>
///     the function to be integrated, tabulated over a mesh.
///   a, b: f64
///     the lower and upper limits of integration
///   sin_coeff: f64
///     the coefficient of sin; 'm' in sin(mx)
///
pub fn filon_tab_sin(ftab: Vec<f64>, a: f64, b: f64, sin_coeff: f64) -> Result<f64, Error> {
    if a == b {
        return Ok(0.0)
    }

    let mesh_size: usize = ftab.len();
    if mesh_size <= 1 || mesh_size % 2 == 0 {
        return Err(Error::new(ErrorKind::InvalidInput, "mesh size must be an odd integer greater than 1."))
    }

    let h: f64 = (b - a) / (mesh_size as f64 - 1.0);
    let theta: f64 = sin_coeff * h;

    // tabulated sine with same mesh as ftab
    let sintab: Vec<f64> = linspace(&a, &b, mesh_size).iter().map(|x| (sin_coeff*x).sin()).collect();

    let (alpha, beta, gamma) = calculate_abg(&theta);

    let s2n: f64 = (0..ftab.len()).step_by(2).map(|x| ftab[x] * sintab[x]).sum::<f64>()
               - 0.5*(ftab[ftab.len()-1]*sintab[ftab.len()-1] + ftab[0]*sintab[0]);
    let s2nm1: f64 = (1..ftab.len()-1).step_by(2).map(|x| ftab[x] * sintab[x]).sum::<f64>();

    let output: f64 = h * (
        alpha * ((ftab[0] * (sin_coeff*a).cos()) - (ftab[ftab.len()-1] * (sin_coeff*b).cos()))
        + beta * s2n
        + gamma * s2nm1
    );

    Ok(output)
}

/// estimates the integral of a function multiplied by cos(mx)
/// over the interval a, b.
///
///  Parameters:
///  ftab: Vec<f64>
///     the function to be integrated, tabulated over a mesh.
///   a, b: f64
///     the lower and upper limits of integration
///   cos_coeff: f64
///     the coefficient of cos; 'm' in cos(mx)
///
pub fn filon_tab_cos(ftab: Vec<f64>, a: f64, b: f64, cos_coeff: f64) -> Result<f64, Error> {
    if a == b {
        return Ok(0.0)
    }

    let mesh_size: usize = ftab.len();
    if mesh_size <= 1 || mesh_size % 2 == 0 {
        return Err(Error::new(ErrorKind::InvalidInput, "mesh size must be an odd integer greater than 1."))
    }

    let h: f64 = (b - a) / (mesh_size as f64 - 1.0);
    let theta: f64 = cos_coeff * h;

    // tabulated cosine with same mesh as ftab
    let costab: Vec<f64> = linspace(&a, &b, mesh_size).iter().map(|x| (cos_coeff*x).cos()).collect();

    let (alpha, beta, gamma) = calculate_abg(&theta);

    let c2n: f64 = (0..ftab.len()).step_by(2).map(|x| ftab[x] * costab[x]).sum::<f64>()
          - 0.5*(ftab[ftab.len()-1]*costab[ftab.len()-1] + ftab[0]*costab[0]);
    let c2nm1: f64 = (1..ftab.len()-1).step_by(2).map(|x| ftab[x] * costab[x]).sum::<f64>();

    let output: f64 = h * (
        alpha * ((ftab[ftab.len()-1] * (cos_coeff*b).sin()) - (ftab[0] * (cos_coeff*a).sin()))
        + beta * c2n
        + gamma * c2nm1
    );

    Ok(output)
}

fn linspace(a: &f64, b: &f64, num_steps: usize) -> Vec<f64>{

    let step_size: f64 = (b - a) / (num_steps as f64 - 1.0);
    let mut lspace: Vec<f64> = Vec::new();
    for n in 0..num_steps {
        lspace.push(a + step_size * n as f64)
    }
    lspace
}

fn calculate_abg(theta: &f64) -> (f64, f64, f64) {
    // for small theta, using a power series gives
    // a more accurate result, at least on the
    // ILLIAC II according to Fosdick and Chase
    if theta.abs() <= 1.0/6.0 {
        (2.0 * (theta.powi(3)) / 45.0
        - 2.0 * (theta.powi(5)) / 315.0
        + 2.0 * (theta.powi(7)) / 4725.0,
        2.0/3.0
        + 2.0 * theta.powi(2) / 15.0
        - 4.0 * theta.powi(4) / 105.0
        + 2.0 * theta.powi(6) / 567.0
        - 4.0 * theta.powi(8) / 22275.0,
        4.0/3.0
        - 2.0 * theta.powi(2) / 15.0
        + theta.powi(4) / 210.0
        - theta.powi(6) / 11340.0
    )

    } else {
        let sint: f64 = theta.sin();
        let cost: f64 = theta.cos();
        ((theta.powi(2) + theta * sint * cost
        - 2.0 * sint.powi(2)) / theta.powi(3),
        (2.0 * theta + 2.0 * theta * cost.powi(2)
        - 4.0 * sint * cost) / theta.powi(3),
        (4.0 * (sint - theta * cost) / theta.powi(3))
    )
    }
}
