# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['essencia_pack']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.63.0,<0.64.0']

setup_kwargs = {
    'name': 'essencia-pack',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'arantesdv',
    'author_email': 'arantesdv@me.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
