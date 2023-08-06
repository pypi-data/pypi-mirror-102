# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simpleicons', 'simpleicons.icons']

package_data = \
{'': ['*'], 'simpleicons': ['_data/*']}

install_requires = \
['Pillow>=8.2.0,<9.0.0', 'reportlab>=3.5.67,<4.0.0', 'svglib>=1.1.0,<2.0.0']

entry_points = \
{'console_scripts': ['generate = scripts.build_package:build']}

setup_kwargs = {
    'name': 'simpleicons',
    'version': '4.20.0',
    'description': 'Use a wide-range of icons derived from the simple-icons/simple-icons repo in python.',
    'long_description': None,
    'author': 'Sachin Raja',
    'author_email': 'sachinraja2349@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
