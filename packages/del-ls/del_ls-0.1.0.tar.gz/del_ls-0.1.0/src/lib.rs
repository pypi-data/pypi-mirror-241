use numpy::{PyReadonlyArray1, PyReadwriteArray1};
use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
#[pyo3(name = "del_ls")]
fn del_ls_(_py: Python, m: &PyModule) -> PyResult<()> {

    #[pyfn(m)]
    fn gemv(
        row2idx: PyReadonlyArray1<usize>,
        idx2col: PyReadonlyArray1<usize>,
        row2val: PyReadonlyArray1<f64>,
        idx2val: PyReadonlyArray1<f64>,
        alpha: f64,
        x_vec: PyReadonlyArray1<f64>,
        beta: f64,
        mut y_vec: PyReadwriteArray1<f64>) {
        let num_blk = row2idx.len() - 1;
        assert_eq!(y_vec.len(), num_blk);
        let y_vec = y_vec.as_slice_mut().unwrap();
        let row2idx = row2idx.as_slice().unwrap();
        let idx2col = idx2col.as_slice().unwrap();
        let idx2val = idx2val.as_slice().unwrap();
        let row2val = row2val.as_slice().unwrap();
        let x_vec = x_vec.as_slice().unwrap();
        for m in  y_vec.iter_mut() { *m *= beta; };
        for iblk in 0..num_blk {
            for icrs in row2idx[iblk]..row2idx[iblk + 1] {
                let jblk0 = idx2col[icrs];
                y_vec[iblk] += alpha * idx2val[icrs] * x_vec[jblk0];
            }
            y_vec[iblk] += alpha * row2val[iblk] * x_vec[iblk];
        }
    }
    Ok(())
}