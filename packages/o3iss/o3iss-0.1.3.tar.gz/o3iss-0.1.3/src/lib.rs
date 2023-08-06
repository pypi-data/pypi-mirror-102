use array2d::Array2D;
use cpython::{py_fn, py_module_initializer, PyResult, Python};
use std::collections::VecDeque;

const UISIZE: u32 = std::mem::size_of::<usize>() as u32 * 8;

py_module_initializer!(o3iss, |py, m| {
    m.add(py, "__doc__", "Rust implementation of ISS")?;
    m.add(
        py,
        "compute",
        py_fn!(py, compute_py(x: Vec<f64>, level: u32)),
    )?;
    Ok(())
});

fn compute_py(_: Python, x: Vec<f64>, level: u32) -> PyResult<Vec<f64>> {
    let out = compute(&x, level);
    Ok(out)
}

fn diff(x: &[f64]) -> Vec<f64> {
    x[1..].iter().zip(x).map(|(&a, &b)| a - b).collect()
}

fn i2c(n: &usize) -> Vec<usize> {
    let mut r = Vec::new();
    let mut y = 1;
    let w = ffs(n);

    for i in 0..w - 1 {
        if (n & (1 << i)) != 0 {
            r.push(y);
            y = 0;
        }
        y += 1;
    }
    r.push(y);
    r.reverse();
    return r;
}

fn ffs(n: &usize) -> usize {
    (UISIZE - n.leading_zeros()) as usize
}

fn parent(n: &usize) -> usize {
    n >> (n.trailing_zeros() + 1)
}

pub fn compute(x: &[f64], level: u32) -> Vec<f64> {
    let mut queue = (0..level).map(|k| 1 << k).collect::<VecDeque<usize>>();
    let dx = diff(x);
    let n = x.len();
    let mut sig = Array2D::filled_with(0f64, 2_usize.pow(level) - 1, n);

    while let Some(next) = &queue.pop_front() {
        let p = *i2c(next).last().unwrap() as i32;
        let m = i2c(next).len();
        if m > 1 {
            for (k, z) in dx[m - 1..].iter().map(|&a| a.powi(p)).enumerate() {
                sig[(next - 1, k + m)] =
                    sig[(next - 1, k + m - 1)] + sig[(parent(next) - 1, k + m - 1)] * z;
            }
        } else {
            for (k, z) in dx[m - 1..].iter().map(|&a| a.powi(p)).enumerate() {
                sig[(next - 1, k + m)] = sig[(next - 1, k + m - 1)] + z;
            }
        }

        for r in 0..level.checked_sub(ffs(&next) as u32).unwrap() {
            queue.push_back(((next << 1) + 1) << r);
        }
    }
    sig.column_iter(n - 1).copied().collect::<Vec<f64>>()
}
