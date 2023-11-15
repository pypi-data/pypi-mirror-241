// Copyright ©, 2023, Lightspark Group, Inc. - All Rights Reserved
//! Bitcoin Rust functions to the Python interpreter.
use std::borrow::Cow;

use psbt::Tx;
use pyo3::{exceptions::PyRuntimeError, prelude::*};

/// Partially Signed Bitcoin Transactions
pub mod psbt;

#[pyfunction]
fn psbt_bytes_to_tx(psbt: Vec<u8>, address: String, fee_offset_sat: u64) -> PyResult<Tx> {
    let tx = psbt::psbt_bytes_to_tx(psbt, address, fee_offset_sat)
        .map_err(|err| PyRuntimeError::new_err(err.to_string()))?;
    Ok(tx)
}

#[pyfunction]
fn generate_sighash(
    tx: Tx,
    input_idx: usize,
    witness_script: Vec<u8>,
    amount_sats: u64,
) -> PyResult<Cow<'static, [u8]>> {
    let sighash = psbt::generate_sighash(tx.psbt, input_idx, witness_script, amount_sats)
        .map_err(|err| PyRuntimeError::new_err(err.to_string()))?;
    // bytes type for pyo3
    Ok(Cow::from(sighash.to_vec()))
}

#[pyfunction]
fn signed_serialized_tx(
    tx: Tx,
    signatures: Vec<Vec<u8>>,
    scripts: Vec<Vec<u8>>,
) -> PyResult<Cow<'static, [u8]>> {
    let tx = psbt::signed_serialized_tx(tx, signatures, scripts)
        .map_err(|err| PyRuntimeError::new_err(err.to_string()))?;
    // bytes type for pyo3
    Ok(Cow::from(tx))
}

/// A Python module implemented in Rust.
#[pymodule]
fn lightspark_bitcoin_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(psbt_bytes_to_tx, m)?)?;
    m.add_function(wrap_pyfunction!(generate_sighash, m)?)?;
    m.add_function(wrap_pyfunction!(signed_serialized_tx, m)?)?;
    Ok(())
}
