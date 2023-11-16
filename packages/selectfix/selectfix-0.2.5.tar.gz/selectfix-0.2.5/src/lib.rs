/// This is a python module library for a constraints function to fix selected variables to constant variables.
///
/// # Examples
/// ## Basic usage
/// ```py
/// selectfix = SelectFix(1, ["x1", "x2", "x3"], [], 0.0, {}, None, 0.0)
/// ```
/// This declaration means creating a function to calculate the penalty
/// for fixing one variable from x1,x2,x3 to 0.
/// That is, if x is given the following values, the penalty is zero because x2 is zero.
/// ```py
/// x = {"x1": 1.0, "x2": 0.0, "x3": 3.0}
/// selectfix(x) # 0.0
/// ```
/// However, if none of the variables are zero, as shown below,
/// The penalty is calculated according to the variable closest to zero.
/// ```py
/// x = {"x1": 1.0, "x2": 2.0, "x3": 3.0}
/// selectfix(x) # -1.0
/// ```
/// The all-fixed variables are also ok.
/// ```py
/// x = {"x1": 0.0, "x2": 0.0, "x3": 0.0}
/// selectfix(x) # 0.0
/// ```
///
/// ## Excluded unfixed combinations
/// You can set a combination of variables that you do not want to include in an unfixed variable.
/// For example, the following declaration will fix one variable among x1, x2, and x3 to 0,
/// and penalize the existence of the pair x1, x2 in the unfixed variable.
/// ```py
/// selectfix = SelectFix(1, ["x1", "x2", "x3"], [["x1", "x2"]], 0.0, {}, None, 0.0)
/// ```
/// This will result in a penalty in x as follows.
/// ```py
/// x = {"x1": 1.0, "x2": 2.0, "x3": 0.0}
/// selectfix(x) # -1.0
/// ```
/// However, if x1 is fixed to 0, the penalty will be zero.
/// ```py
/// x = {"x1": 0.0, "x2": 2.0, "x3": 0.0}
/// selectfix(x) # 0.0
/// ```
///
/// ## Ranges
/// A range of values can be penalized for an unfixed variable.
/// ```py
/// selectfix = SelectFix(1, ["x1", "x2", "x3"], [], 0.0, {"x1": (1.0, 2.0), "x2": (3.0, 4.0)}, 1, 0.0)
/// ```
/// This adds a penalty if x1 is chosen as an unfixed variable and x1 is not in the range 1.0~2.0.
/// ```py
/// x = {"x1": 3.0, "x2": 3.0, "x3": 0.0}
/// selectfix(x) # -1.0
/// x = {"x1": 1.5, "x2": 3.0, "x3": 0.0}
/// selectfix(x) # 0.0
/// ```
///
/// ## Maximum number of fixed variables
/// You can set the number of maximum number of fixed variables.
/// ```py
/// selectfix = SelectFix(1, ["x1", "x2", "x3"], [], 0.0, {"x1": (1.0, 2.0), "x2": (3.0, 4.0)}, 2, 0.0)
/// ```
/// In this case, if they are all fixed, a penalty is incurred due to the `range` setting,
/// but if only one of x1 or x2 deviates from the `range`, no penalty is incurred.
/// ```py
/// x = {"x1": 0.0, "x2": 0.0, "x3": 0.0}
/// selectfix(x) # -1.0
/// x = {"x1": 0.0, "x2": 3.0, "x3": 0.0}
/// selectfix(x) # 0.0
/// ```
///
use indexmap::IndexMap;
use pyo3::prelude::*;
use pyo3::types::PyBytes;

use anyhow::Result;
use bincode::{deserialize, serialize};
use ordered_float::OrderedFloat;
use serde::{Deserialize, Serialize};
use std::cmp;
use std::collections::HashMap;

/// A selector for the fixed value.
/// This class selects the variables which are closest to the fixed value.
#[derive(Serialize, Deserialize)]
#[pyclass(module = "selectfix")]
struct Selector {
    #[pyo3(get)]
    n_select_min: usize,
    #[pyo3(get)]
    candidates: Vec<String>,
    #[pyo3(get)]
    excluded_unfixed_combinations: Vec<Vec<String>>,
    #[pyo3(get)]
    fixed_val: f64,
    #[pyo3(get)]
    ranges: HashMap<String, (f64, f64)>,
    #[pyo3(get)]
    n_select_max: Option<usize>,
    #[pyo3(get)]
    eps: f64,
}

impl Selector {
    fn is_excluded(&self, names: Vec<&String>) -> bool {
        self.excluded_unfixed_combinations
            .iter()
            .any(|ex| ex.iter().all(|e| names.contains(&e)))
    }
    fn search_free(
        &self,
        open_idxs: Vec<usize>,
        names: &Vec<String>,
        close_idxs: Vec<usize>,
    ) -> (Vec<usize>, bool) {
        if open_idxs.len() <= self.n_select_min {
            return ([close_idxs, open_idxs].concat(), true);
        }
        for (i, &k) in open_idxs.iter().enumerate() {
            let close_idxs_k = [close_idxs.clone(), vec![k]].concat();
            if self.is_excluded(close_idxs_k.iter().map(|&j| &names[j]).collect::<Vec<_>>()) {
                continue;
            }
            let mut tmp_open_idxs = open_idxs.clone();
            tmp_open_idxs.remove(i);
            let (tmp_searched, res) = self.search_free(tmp_open_idxs, names, close_idxs_k);
            if res {
                return (tmp_searched, res);
            }
        }
        (close_idxs, false)
    }
    fn compute_indices(
        &self,
        xdic: &IndexMap<String, f64>,
    ) -> Result<(Vec<usize>, Vec<OrderedFloat<f64>>)> {
        let xdic_new = if self.candidates.is_empty() {
            xdic.clone()
        } else {
            // Extract the candidates from xdic.
            self.candidates
                .iter()
                .map(|can| (can.clone(), xdic[can]))
                .collect::<IndexMap<_, _>>()
        };
        let violations = xdic_new
            .iter()
            .map(|(_, &x)| {
                cmp::min(
                    OrderedFloat(-(x - self.fixed_val).abs() + self.eps),
                    OrderedFloat(0.0),
                )
            })
            .collect::<Vec<_>>();
        let mut indices = (0..violations.len()).collect::<Vec<_>>();
        indices.sort_by(|&i, &j| violations[i].cmp(&violations[j]));
        if self.excluded_unfixed_combinations.len() > 0 {
            let (searched, res) =
                self.search_free(indices.clone(), &xdic_new.keys().cloned().collect(), vec![]);
            if !res {
                return Err(anyhow::anyhow!(
                    "Not found the selections with the given excluded_unfixed_combinations.",
                ));
            }
            indices = searched;
        }
        indices.reverse();
        Ok((indices, violations))
    }
    fn compute_additional_penalties(
        &self,
        xdic: &IndexMap<String, f64>,
        indices: &Vec<usize>,
    ) -> (Vec<OrderedFloat<f64>>, Vec<usize>) {
        let num_candidates = if self.candidates.is_empty() {
            xdic.len()
        } else {
            self.candidates.len()
        };
        let mut additional_penalty_indices = (self.n_select_min..indices.len()).collect::<Vec<_>>();
        let additional_penalties = additional_penalty_indices
            .iter()
            .map(|i| {
                let key = &self.candidates[indices[*i]];
                if let (Some(range), Some(x)) = (self.ranges.get(key), xdic.get(key)) {
                    if range.0 <= *x && *x <= range.1 {
                        OrderedFloat(0.0)
                    } else {
                        cmp::min(
                            OrderedFloat((range.0 - x).abs()),
                            OrderedFloat((range.1 - x).abs()),
                        )
                    }
                } else {
                    OrderedFloat(0.0)
                }
            })
            .collect::<Vec<_>>();
        additional_penalty_indices.sort_by_key(|i| additional_penalties[*i - self.n_select_min]);
        let additional_penalty_indices = additional_penalty_indices
            .into_iter()
            .take(num_candidates - self.n_select_max.unwrap_or(num_candidates))
            .collect::<Vec<_>>();
        (
            additional_penalty_indices
                .iter()
                .map(|i| additional_penalties[*i - self.n_select_min])
                .collect::<Vec<_>>(),
            additional_penalty_indices,
        )
    }
}

#[pymethods]
impl Selector {
    /// Create a new selector.
    ///
    /// # Arguments
    /// * `n_select_min` - The minimum number of variables to be selected to fix.
    /// * `candidates` - Candidates for selection.
    /// * `excluded_unfixed_combinations` - Combinations you want to exclude among unfixed variables.
    /// * `fixed_val` - Target value of variable to be fixed.
    /// * `ranges` - Range to be set on unfixed variables.
    /// * `n_select_max` - The maximum number of variable to be selected to fix. If None, n_select_max = len(candidates).
    /// * `eps` - Tolerance for fixed variables and fixed_val.
    #[new]
    fn new(
        n_select_min: usize,
        candidates: Vec<String>,
        excluded_unfixed_combinations: Vec<Vec<String>>,
        fixed_val: f64,
        ranges: HashMap<String, (f64, f64)>,
        n_select_max: Option<usize>,
        eps: f64,
    ) -> Self {
        Selector {
            n_select_min: n_select_min,
            candidates: candidates,
            excluded_unfixed_combinations: excluded_unfixed_combinations,
            fixed_val: fixed_val,
            ranges: ranges,
            n_select_max: n_select_max,
            eps: eps,
        }
    }
    fn __call__(&self, xdic: IndexMap<String, f64>) -> PyResult<f64> {
        let (indices, violations) = self
            .compute_indices(&xdic)
            .map_err(|e| pyo3::exceptions::PyValueError::new_err(e.to_string()))?;
        // Compute the additional penalty.
        // This is the penalty for the variables which are not selected.
        // The penalty is the minimum of the distance from the fixed value to the lower and upper bounds.
        let additional: f64 = if self.candidates.is_empty() || self.ranges.is_empty() {
            0.0
        } else {
            self.compute_additional_penalties(&xdic, &indices)
                .0
                .iter()
                .map(|p| p.0)
                .sum()
        };
        Ok((0..self.n_select_min)
            .map(|i| f64::from(violations[indices[i]]))
            .sum::<f64>()
            - additional)
    }
    fn jacobian(&self, xdic: IndexMap<String, f64>) -> PyResult<Vec<f64>> {
        let ndim = xdic.len();
        let (indices, _) = self
            .compute_indices(&xdic)
            .map_err(|e| pyo3::exceptions::PyValueError::new_err(e.to_string()))?;
        let mut jac = vec![0.0; ndim];
        for i in 0..self.n_select_min {
            jac[indices[i]] = 1.0;
        }
        if self.candidates.is_empty() || self.ranges.is_empty() {
            return Ok(jac);
        }
        let (additional_penalties, additional_penalty_indices) =
            self.compute_additional_penalties(&xdic, &indices);
        for (i, idx) in additional_penalty_indices.iter().enumerate() {
            jac[indices[*idx]] = if additional_penalties[i].0 == 0.0 {
                0.0
            } else {
                additional_penalties[i].0.signum()
            };
        }
        Ok(jac)
    }
    fn hessian(&self, xdic: IndexMap<String, f64>) -> PyResult<Vec<Vec<f64>>> {
        Ok(vec![vec![0.0; xdic.len()]; xdic.len()])
    }
    fn __setstate__(&mut self, _py: Python, state: &PyBytes) -> PyResult<()> {
        *self = deserialize(state.as_bytes()).unwrap();
        Ok(())
    }
    fn __getstate__<'py>(&self, py: Python<'py>) -> PyResult<&'py PyBytes> {
        Ok(PyBytes::new(py, &serialize(&self).unwrap()))
    }
    pub fn __getnewargs__(
        &self,
    ) -> PyResult<(
        usize,
        Vec<String>,
        Vec<Vec<String>>,
        f64,
        HashMap<String, (f64, f64)>,
        Option<usize>,
        f64,
    )> {
        Ok((
            self.n_select_min,
            self.candidates.clone(),
            self.excluded_unfixed_combinations.clone(),
            self.fixed_val,
            self.ranges.clone(),
            self.n_select_max,
            self.eps,
        ))
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn selectfix(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Selector>()?;
    Ok(())
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_is_excluded() {
        use super::*;
        let selector = Selector::new(
            2,
            vec![
                "a".to_string(),
                "b".to_string(),
                "c".to_string(),
                "d".to_string(),
            ],
            vec![vec!["a".to_string(), "b".to_string()]],
            0.0,
            HashMap::new(),
            None,
            0.0,
        );
        assert_eq!(
            selector.is_excluded(vec![&"a".to_string(), &"b".to_string()]),
            true
        );
        assert_eq!(selector.is_excluded(vec![&"a".to_string()]), false);
        assert_eq!(
            selector.is_excluded(vec![&"a".to_string(), &"c".to_string()]),
            false
        );
    }

    #[test]
    fn test_search_free() {
        use super::*;
        let selector = Selector::new(
            2,
            vec![
                "a".to_string(),
                "b".to_string(),
                "c".to_string(),
                "d".to_string(),
            ],
            vec![vec!["a".to_string(), "b".to_string()]],
            0.0,
            HashMap::new(),
            None,
            0.0,
        );
        let (searched, res) = selector.search_free(
            vec![0, 1, 2, 3],
            &vec![
                "a".to_string(),
                "b".to_string(),
                "c".to_string(),
                "d".to_string(),
            ],
            vec![],
        );
        assert_eq!(res, true);
        assert_eq!(searched, vec![0, 2, 1, 3]);
    }
}
