# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypoints2grid']

package_data = \
{'': ['*'], 'pypoints2grid': ['include/*', 'src/*']}

install_requires = \
['numpy>=1.23.3,<2.0.0', 'pybind11>=2.10.0,<3.0.0']

setup_kwargs = {
    'name': 'pypoints2grid',
    'version': '0.1.1',
    'description': 'implementation of points2grid algorithm',
    'long_description': '# pypoints2grid\nPython library implementing points2grid algorithm (https://www.opentopography.org/otsoftware/points2grid)\n',
    'author': 'Dag Wästberg',
    'author_email': 'dwastberg@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dwastberg/pypoint2grid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
