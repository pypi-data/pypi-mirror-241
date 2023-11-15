use pyo3::prelude::*;
use numpy::{IntoPyArray, PyArray2, PyReadonlyArray2};
use numpy::ndarray::Array2;

#[pyclass(module = "del_cad")]
struct MyClass {
    cad: del_cad::cad2::Cad2,
}

#[pymethods]
impl MyClass {
    #[new]
    fn new() -> Self {
        Self {
            cad: del_cad::cad2::Cad2::new()
        }
    }

    fn add_polygon(
        &mut self,
        _py: Python,
        pos: Vec<f64>) -> usize {
        self.cad.add_polygon(&pos)
    }

    fn triangulation<'py>(
        &self,
        _py: Python<'py>,
        edge_length: f64) -> (&'py PyArray2<usize>,
                              &'py PyArray2<f64>) {
        let mut mesher = del_cad::mesher_cad2::MesherCad2::new();
        mesher.edge_length = edge_length;
        let mesh = mesher.meshing(
            &self.cad);
        let (tri2vtx, vtx2xy) = del_dtri::array_from_2d_dynamic_triangle_mesh(
            &mesh.0, &mesh.2);
        (
            numpy::ndarray::Array2::from_shape_vec(
                (tri2vtx.len() / 3, 3), tri2vtx).unwrap().into_pyarray(_py),
            numpy::ndarray::Array2::from_shape_vec(
                (vtx2xy.len() / 2, 2), vtx2xy).unwrap().into_pyarray(_py)
        )
    }

    fn area_of_face(&self, i0_face: usize) -> f64 {
        self.cad.get_face(i0_face).area()
    }

    #[getter]
    fn get_num_vertex(&self) -> PyResult<usize> {
        Ok(self.cad.vertices.len())
    }
}


/// A Python module implemented in Rust.
#[pymodule]
fn del_cad(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<MyClass>()?;

    #[pyfn(m)]
    pub fn tesselation2d<'a>(
        py: Python<'a>,
        vtx2xy_in: PyReadonlyArray2<'a, f32>) -> (&'a PyArray2<usize>, &'a PyArray2<f32>) {
        let num_vtx = vtx2xy_in.shape()[0];
        let loop2idx = vec!(0, num_vtx);
        let idx2vtx = (0..num_vtx).collect();
        type Vec2 = nalgebra::Vector2<f32>;
        let mut vtx2xy = Vec::<Vec2>::new();
        for ivtx in 0..num_vtx {
            let v0 = Vec2::new(
                *vtx2xy_in.get((ivtx, 0)).unwrap(),
                *vtx2xy_in.get((ivtx, 1)).unwrap());
            vtx2xy.push(v0);
        }
        let mut tri2pnt = Vec::<del_dtri::topology::DynamicTriangle>::new();
        let mut pnt2tri = Vec::<del_dtri::topology::DynamicVertex>::new();
        del_dtri::mesher2::meshing_single_connected_shape2(
            &mut pnt2tri, &mut vtx2xy, &mut tri2pnt,
            &loop2idx, &idx2vtx);
        let mut vtx2xy_out = Vec::<f32>::new();
        for ivtx in 0..vtx2xy.len() {
            vtx2xy_out.push(vtx2xy[ivtx].x);
            vtx2xy_out.push(vtx2xy[ivtx].y);
        }
        let mut tri2vtx_out = Vec::<usize>::new();
        for itri in 0..tri2pnt.len() {
            tri2vtx_out.push(tri2pnt[itri].v[0]);
            tri2vtx_out.push(tri2pnt[itri].v[1]);
            tri2vtx_out.push(tri2pnt[itri].v[2]);
        }
        (
            Array2::from_shape_vec((tri2vtx_out.len() / 3, 3), tri2vtx_out).unwrap().into_pyarray(py),
            Array2::from_shape_vec((vtx2xy_out.len() / 2, 2), vtx2xy_out).unwrap().into_pyarray(py),
        )
    }

    Ok(())
}

