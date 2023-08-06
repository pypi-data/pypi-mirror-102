# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycograph', 'pycograph.helpers', 'pycograph.schemas']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8,<2.0', 'redisgraph>=2.3,<3.0', 'typer==0.3.2']

entry_points = \
{'console_scripts': ['pycograph = pycograph.cli:app']}

setup_kwargs = {
    'name': 'pycograph',
    'version': '0.2.1',
    'description': '',
    'long_description': None,
    'author': 'reka',
    'author_email': 'reka@hey.com',
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
