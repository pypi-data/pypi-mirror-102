# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['logfmt_logger']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'logfmt-logger',
    'version': '0.1.1',
    'description': 'Logger following the logfmt format with sound defaults',
    'long_description': None,
    'author': 'Michael Mercier',
    'author_email': 'michael.mercier@ryax.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
