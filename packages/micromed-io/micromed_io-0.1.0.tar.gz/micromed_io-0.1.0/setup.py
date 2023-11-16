# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['micromed_io']

package_data = \
{'': ['*']}

install_requires = \
['mne>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'micromed-io',
    'version': '0.1.0',
    'description': 'A library to handle Micromed data',
    'long_description': 'None',
    'author': 'Etienne de MONTALIVET',
    'author_email': 'etienne.demontalivet@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
