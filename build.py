from pybind11.setup_helpers import Pybind11Extension, build_ext

def build(setup_kwargs):
    ext_modules = [
        Pybind11Extension("_points2grid", ["ext_points2grid/src/pybind_points2grid.cpp"],
        include_dirs = ["ext_points2grid/include"],
        extra_compile_args=['-std=c++1y']),
    ]
    setup_kwargs.update({
        "ext_modules": ext_modules,
        "zip_safe": False
    })
