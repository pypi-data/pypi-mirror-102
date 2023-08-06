# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_key_auth']

package_data = \
{'': ['*']}

install_requires = \
['starlette==0.13.6']

setup_kwargs = {
    'name': 'fastapi-key-auth',
    'version': '0.2.0',
    'description': 'API key validation Middleware',
    'long_description': None,
    'author': 'Benjamin Ramser',
    'author_email': 'legionaerr@googlemail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
