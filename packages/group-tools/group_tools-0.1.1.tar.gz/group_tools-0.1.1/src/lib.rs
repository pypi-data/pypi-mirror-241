use pyo3::types::PyDict;
use pyo3::prelude::*;
use serde_json::json;

#[pyfunction]
fn group_dict(data: &str) -> PyResult<String> {
    let data: serde_json::Value = serde_json::from_str(data).map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("{}", e)))?;
    let mut result_data = json!({});

    // iterate over data
    for (key, value) in data.as_object().unwrap().iter() {
        if key.contains("___") {
            key.split_once("___").map(|(l, r)| {
                result_data[l][r] = value.clone();
            });
        } else {
            result_data[key] = value.clone();
        }
    }

    Ok(result_data.to_string())
}

// takes dict as input and returns grouped dict like in group_dict
#[pyfunction]
fn group_dict2(data: &PyDict) -> PyResult<PyObject> {
    let result_data = PyDict::new(data.py());

    // iterate over data
    for (key, value) in data.iter() {
        if key.contains("___")? {
            key.to_string().split_once("___").map(|(l, r)| {
                if result_data.get_item(l).expect("").is_none() {
                    let _result = result_data.set_item(l, PyDict::new(data.py()));
                }
                let item = result_data.get_item(l).unwrap().unwrap();
                let _ = item.set_item(r, value);
            });

        } else {
            result_data.set_item(key, value)?;
        }
    }
    Ok(result_data.to_object(data.py()))
}

#[pymodule]
fn group_tools(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(group_dict, m)?)?;
    m.add_function(wrap_pyfunction!(group_dict2, m)?)?;

    Ok(())
}
