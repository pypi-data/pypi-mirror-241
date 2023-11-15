use pyo3::{prelude::*, exceptions::PyValueError, types::{PyTuple, PyDict}};
use ::reaction_system::{ReactionSystem as RS, RsFunction as RF, Reaction as ReactionStruct, RsMinimize, EspressoError};

struct EspressoErrorPyO3(EspressoError);

impl From<EspressoErrorPyO3> for PyErr {
    fn from(error: EspressoErrorPyO3) -> Self {
        PyValueError::new_err(format!("{:?}", error.0))
    }
}

impl From<EspressoError> for EspressoErrorPyO3 {
    fn from(other: EspressoError) -> Self {
        Self(other)
    }
}


#[pyclass]
#[derive(Clone, Debug)]
struct Reaction (ReactionStruct<Vec<usize>>);

#[pymethods]
impl Reaction {
  #[new]
  fn new(reactants: Vec<usize>, inhibitors: Vec<usize>, products: Vec<usize>) -> Self {
    Self (ReactionStruct { reactants, inhibitors, products })
  }

  fn enabled(&self, state: Vec<usize>) -> bool {
    // This is a pretty awful way of doing this, but it's probably still faster than anything you can do in python
    let bg_size = self.min_bg_size().max(*state.iter().max().unwrap_or(&0));
    if bg_size == 0 {
      return true;
    }
    let mut rs = RS::simple_new(bg_size);
    rs.push(self.0.clone());
    rs.enabled(state)
  }

  fn reactants(&self) -> Vec<usize> {
    self.0.reactants.clone()
  }

  fn inhibitors(&self) -> Vec<usize> {
    self.0.reactants.clone()
  }

  fn products(&self) -> Vec<usize> {
    self.0.reactants.clone()
  }

  // returns the largest element used in the reaction
  fn min_bg_size(&self) -> usize {
    let r_max = self.0.reactants.iter().max().unwrap_or(&0);
    let i_max = self.0.inhibitors.iter().max().unwrap_or(&0);
    let p_max = self.0.products.iter().max().unwrap_or(&0);
    *r_max.max(i_max.max(p_max))
  }

  fn deconstruct(&self) -> (Vec<usize>, Vec<usize>, Vec<usize>) {
    self.0.clone().deconstruct()
  }

  fn result(&self, state: Vec<usize>) -> Vec<usize> {
    match self.enabled(state) {
      true => self.products().clone(),
      false => vec![],
    }
  }

  fn __str__(&self) -> String {
    format!("({{{}}}, {{{}}}, {{{}}})", 
      format_vec(&self.0.reactants),
      format_vec(&self.0.inhibitors),
      format_vec(&self.0.products),
    )
  }

  fn __repr__(&self) -> String {
    self.__str__()
  }
}

fn format_vec(v: &Vec<usize>) -> String {
  v.iter().map(|i| i.to_string()).collect::<Vec<String>>().join(", ")
}


#[pyclass]
#[derive(Clone, Debug)]
struct ReactionSystem (RS);

#[pymethods]
impl ReactionSystem {
  #[new]
  fn new(bg_size: usize) -> Self {
    ReactionSystem (RS::simple_new(bg_size))
  }

  #[staticmethod]
  fn from_cycle(cycle: Vec<Vec<usize>>, bg_size: Option<usize>) -> PyResult<Self> {
    let bg_size = match bg_size {
      None => cycle.iter().filter_map(|v| v.iter().max()).max().ok_or(PyValueError::new_err("Could not determine bg_size from cycle!"))?.clone(),
      Some(b) => b,
    };
    Ok( ReactionSystem(RS::simple_cycle(bg_size, cycle)) )
  }

  #[pyo3(signature = (*py_args))]
  fn push(&mut self, py_args: &PyTuple) -> PyResult<bool> {
    let arg1 = py_args.get_item(0)?;
    if let Ok(reaction) = arg1.extract::<Reaction>() {
      Ok(self.0.push(reaction.0))
    } else {
      let reactants = arg1.extract::<Vec<usize>>()?;
      let inhibitors = py_args.get_item(1)?.extract::<Vec<usize>>()?;
      let products = py_args.get_item(2)?.extract::<Vec<usize>>()?;
      Ok(self.0.push(ReactionStruct { reactants, inhibitors, products }))
    }
  }

  fn push_state(&mut self, state: Vec<usize>, products: Vec<usize>) {
    self.0.push_state(state, products)
  }

  #[pyo3(signature = (*py_args))]
  fn remove(&mut self, py_args: &PyTuple) -> PyResult<()> {
    let arg1 = py_args.get_item(0)?;
    if let Ok(reaction) = arg1.extract::<Reaction>() {
      self.0.remove(reaction.0);
    } else {
      let reactants = arg1.extract::<Vec<usize>>()?;
      let inhibitors = py_args.get_item(1)?.extract::<Vec<usize>>()?;
      let products = py_args.get_item(2)?.extract::<Vec<usize>>()?;
      self.0.remove(ReactionStruct { reactants, inhibitors, products });
    }
    Ok(())
  }

  fn result(&self, state: Vec<usize>) -> Vec<usize> {
    self.0.result(state).collect()
  }

  fn enabled(&self, state: Vec<usize>) -> bool {
    self.0.enabled(state)
  }

  fn reactions(&self) -> Vec<Reaction> {
    self.0.reactions().map(|f| {
      let (r, i, p) = f.deconstruct();
      Reaction::new(r.collect(), i.collect(), p.collect())
    }).collect()
  }

  fn degree(&self) -> usize {
    self.0.degree()
  }

  fn rank(&self) -> usize {
    self.0.rank()
  }

  fn minimize_rank(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.minimize_rank()?;
    Ok(Self (rs))
  }

  fn minimize_rank_exact(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.minimize_rank_exact()?;
    Ok(Self (rs))
  }

  fn minimize_degree(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.minimize_degree()?;
    Ok(Self (rs))
  }

  fn complement(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.complement()?;
    Ok(Self (rs))
  }

  fn primes(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.primes()?;
    Ok(Self (rs))
  }

  fn essential_primes(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.essential_primes()?;
    Ok(Self (rs))
  }

  fn achieve_rank_degree(&self, rank_bound: Option<usize>, degree_bound: Option<usize>) -> Result<Option<ReactionSystem>, EspressoErrorPyO3> {
    let r = self.0.achieve_rank_degree(rank_bound, degree_bound)?;
    Ok(r.map(|rs| Self (rs)))
  }

  fn __str__(&self) -> String {
    format!("{}", self.0)
  }

  fn __repr__(&self) -> String {
    format!("[ReactionSystem@{self:p};bg_size:{};reactions:{}]", self.0.bg_size(), self.0.rank())
  }
}

#[pyclass]
#[derive(Clone, Debug)]
struct RsFunction (RF);

#[pymethods]
impl RsFunction {
  #[new]
  fn new(bg_size: usize) -> Self {
    Self (RF::simple_new(bg_size))
  }

  #[staticmethod]
  fn from_cycle(cycle: Vec<Vec<usize>>, bg_size: Option<usize>) -> PyResult<Self> {
    let bg_size = match bg_size {
      None => cycle.iter().filter_map(|v| v.iter().max()).max().ok_or(PyValueError::new_err("Could not determine bg_size from cycle!"))?.clone(),
      Some(b) => b,
    };
    Ok( Self(RF::simple_cycle(bg_size, cycle.into_iter())) )
  }

  fn add(&mut self, input: Vec<usize>, output: Vec<usize>) -> Option<Vec<usize>> {
    self.0.add(input, output)
  }

  fn remove(&mut self, input: Vec<usize>) -> Option<Vec<usize>> {
    self.0.remove(input)
  }

  fn map<'a>(&self, py: Python<'a>) -> PyResult<&'a PyDict> {
    let map = PyDict::new(py);
    for (i, o) in self.0.map_iter() {
      let i: Vec<usize> = i.collect();
      let i = PyTuple::new(py, i);
      let o: Vec<usize> = o.collect();
      map.set_item(i, o)?;
    }
    Ok(map)
  }

  fn support(&self) -> Vec<Vec<usize>> {
    self.0.support().map(|i| i.collect()).collect()
  }

  fn mapped_domain(&self) -> Vec<Vec<usize>> {
    self.0.mapped_domain().map(|i| i.collect()).collect()
  }

  fn minimize_rank(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.minimize_rank()?;
    Ok(ReactionSystem (rs))
  }

  fn minimize_rank_exact(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.minimize_rank_exact()?;
    Ok(ReactionSystem (rs))
  }

  fn minimize_degree(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.minimize_degree()?;
    Ok(ReactionSystem (rs))
  }

  fn complement(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.complement()?;
    Ok(ReactionSystem (rs))
  }

  fn primes(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.primes()?;
    Ok(ReactionSystem (rs))
  }

  fn essential_primes(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.essential_primes()?;
    Ok(ReactionSystem (rs))
  }

  fn achieve_rank_degree(&self, rank_bound: Option<usize>, degree_bound: Option<usize>) -> Result<Option<ReactionSystem>, EspressoErrorPyO3> {
    let r = self.0.achieve_rank_degree(degree_bound, rank_bound)?;
    Ok(r.map(|rs| ReactionSystem (rs)))
  }

  fn __str__(&self) -> String {
    format!("{}", self.0)
  }

  fn __repr__(&self) -> String {
    format!("[RsFunction@{self:p};bg_size:{};states-defined:{}]", self.0.bg_size(), self.0.len())
  }

  fn __len__(&self) -> usize {
    self.0.len()
  }
}


/// A Python module implemented in Rust.
#[pymodule]
fn reaction_system(_py: Python, m: &PyModule) -> PyResult<()> {
  m.add_class::<ReactionSystem>()?;
  m.add_class::<RsFunction>()?;
  m.add_class::<Reaction>()?;
  Ok(())
}
