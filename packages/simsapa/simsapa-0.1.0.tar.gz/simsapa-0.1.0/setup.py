# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simsapa', 'simsapa.app', 'simsapa.layouts']

package_data = \
{'': ['*'], 'simsapa': ['assets/icons/png/*', 'assets/icons/svg/*']}

install_requires = \
['Markdown>=3.3.4,<4.0.0',
 'PyMuPDF>=1.18.12,<2.0.0',
 'PySimpleGUI==4.38.0',
 'SQLAlchemy>=1.4.6,<2.0.0',
 'pillow>=8.2.0,<9.0.0',
 'requests==2.25.1',
 'tkinterweb==3.0.0']

setup_kwargs = {
    'name': 'simsapa',
    'version': '0.1.0',
    'description': 'Simsapa Dhamma Reader',
    'long_description': None,
    'author': 'Gambhiro',
    'author_email': 'gambhiro.bhikkhu.85@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
