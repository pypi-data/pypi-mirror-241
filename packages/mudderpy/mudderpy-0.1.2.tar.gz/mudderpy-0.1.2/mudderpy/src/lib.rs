use std::num::NonZeroUsize;
use std::str::FromStr;

use ::mudder::error::CreationError;
use ::mudder::error::GenerationError;
use ::mudder::SymbolTable as NativeSymbolTable;
use pyo3::create_exception;
use pyo3::exceptions;
use pyo3::prelude::*;

create_exception!(mymodule, PyCreationError, exceptions::PyException);

fn creation_error_to_py(err: CreationError) -> PyErr {
    PyErr::new::<PyCreationError, _>(format!("SymbolTable creation failed: {}", err))
}

fn generation_error_to_py(err: GenerationError) -> PyErr {
    PyErr::new::<exceptions::PyRuntimeError, _>(format!("Generation failed: {}", err))
}

#[pyclass]
pub struct SymbolTable {
    table: NativeSymbolTable,
}

#[pymethods]
impl SymbolTable {
    #[new]
    fn new(symbols: &str) -> PyResult<Self> {
        match NativeSymbolTable::from_str(symbols) {
            Ok(r) => Ok(Self { table: r }),
            Err(e) => Err(creation_error_to_py(e)),
        }
    }

    pub fn mudder(&self, a: &str, b: &str, amount: usize) -> PyResult<Vec<String>> {
        let amount = NonZeroUsize::new(amount)
            .ok_or_else(|| PyErr::new::<exceptions::PyValueError, _>("Amount must be non-zero"))?;

        match self.table.mudder(a, b, amount) {
            Ok(r) => Ok(r),
            Err(e) => Err(generation_error_to_py(e)),
        }
    }

    pub fn mudder_one(&self, a: &str, b: &str) -> PyResult<String> {
        match self.table.mudder_one(a, b) {
            Ok(r) => Ok(r),
            Err(e) => Err(generation_error_to_py(e)),
        }
    }

    pub fn generate(&self, amount: usize) -> PyResult<Vec<String>> {
        let amount = NonZeroUsize::new(amount)
            .ok_or_else(|| PyErr::new::<exceptions::PyValueError, _>("Amount must be non-zero"))?;

        match self.table.generate(amount) {
            Ok(r) => Ok(r),
            Err(e) => Err(generation_error_to_py(e)),
        }
    }

    #[staticmethod]
    pub fn alphabet() -> PyResult<Self> {
        Ok(Self {
            table: NativeSymbolTable::alphabet(),
        })
    }

    #[staticmethod]
    pub fn base36() -> PyResult<Self> {
        Ok(Self {
            table: NativeSymbolTable::base36(),
        })
    }

    #[staticmethod]
    pub fn base62() -> PyResult<Self> {
        Ok(Self {
            table: NativeSymbolTable::base62(),
        })
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn mudderpy(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<SymbolTable>()?;
    Ok(())
}
