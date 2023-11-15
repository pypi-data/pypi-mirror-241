# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pflops']

package_data = \
{'': ['*']}

install_requires = \
['requests-toolbelt>=1.0.0,<2.0.0',
 'requests>=2.31.0,<3.0.0',
 'typer[all]>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['pflops = pflops.main:app']}

setup_kwargs = {
    'name': 'pflops',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Petaflops CLI\n',
    'author': 'Gunwoo Kim',
    'author_email': 'gunwoo@petaflops.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
