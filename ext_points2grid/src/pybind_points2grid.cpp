#include <limits>
#include <math.h>
#include <stddef.h>

#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "Interpolator.h"

using namespace std;
namespace py = pybind11;

py::array_t<double> _points2grid(py::array_t<double> pts, double cell_size,
                                 double x_min, double y_min, double x_max,
                                 double y_max, double radius, int window_size,
                                 bool check_bounds, bool verbose) {

  auto pts_r = pts.unchecked<2>();
  size_t pt_count = pts_r.shape(0);

  if (radius <= 0) {
    radius = std::sqrt(2.0) * cell_size;
  }

  if (cell_size <= 0) {
    domain_error("Cell size must be great than 0");
  }

  // The user defines the edges of the bounding box, here we want the min/max
  // values to represent the centers of the edge cells
  double orig_x_min = x_min;
  double orig_y_min = y_min;
  double orig_x_max = x_max;
  double orig_y_max = y_max;

  x_min = x_min + cell_size / 2.0;
  x_max = x_max - cell_size / 2.0;
  y_min = y_min + cell_size / 2.0;
  y_max = y_max - cell_size / 2.0;

  size_t size_x = (size_t)(std::ceil((x_max - x_min) / cell_size)) + 1;
  size_t size_y = (size_t)(std::ceil((y_max - y_min) / cell_size)) + 1;

  if (verbose)
    py::print("generating grid with size (", size_x, ",", size_y, ")");
  auto grid_interp = Interpolator(cell_size, cell_size, size_x, size_y, radius,
                                  x_min, x_max, y_min, y_max, window_size);

  grid_interp.init();
  double x, y, z;
  for (size_t i = 0; i < pt_count; i++) {
    x = pts_r(i, 0);
    y = pts_r(i, 1);
    z = pts_r(i, 2);
    if (check_bounds) {
      if (x < orig_x_min || x > orig_x_max || y < orig_y_min || y > orig_y_max)
        continue;
    }
    grid_interp.update(x, y, z);
  }
  grid_interp.calculate_grid_values();

  py::array_t<double> result = py::array_t<double>(size_x * size_y);
  py::buffer_info result_buf = result.request();
  double *result_ptr = (double *)result_buf.ptr;
  for (size_t idx = 0; idx < size_x; idx++) {
    for (size_t idy = 0; idy < size_y; idy++) {
      auto gp = grid_interp.get_grid_point(idx, idy);
      result_ptr[idx * size_y + idy] = gp.Zidw;
    }
  }
  result.resize({size_x, size_y});
  return result;
}

PYBIND11_MODULE(_points2grid, m) {
  m.doc() = "imple  mentation of points2grid algorithm";
  m.def("_points2grid", &_points2grid, "generate grid from pointcloud");
}