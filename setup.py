# -*- coding: utf-8 -*-
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext


packages = \
['pypoints2grid']

package_data = \
{'': ['*'], 'pypoints2grid': ['src/*']}

install_requires = \
['numpy>=1.23.3,<2.0.0', 'pybind11>=2.10.0,<3.0.0']

setup_kwargs = {
    'name': 'pypoints2grid',
    'version': '0.2.3',
    'description': 'implementation of points2grid algorithm',
    'long_description': '# pypoints2grid\nPython library implementing points2grid algorithm (https://www.opentopography.org/otsoftware/points2grid)\n',
    'author': 'Dag Wästberg',
    'author_email': 'dwastberg@gmail.com',
    'url': 'https://github.com/dwastberg/pypoint2grid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}
def build(setup_kwargs):
    ext_modules = [
        Pybind11Extension("_points2grid", ["src/pybind_points2grid.cpp"],
                          include_dirs = ["src/include"],
                          extra_compile_args=['-std=c++1y']),
    ]
    setup_kwargs.update({
        "ext_modules": ext_modules,
        "zip_safe": False
    })
build(setup_kwargs)

setup(**setup_kwargs)
