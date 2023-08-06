# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['amplitude_python_sdk',
 'amplitude_python_sdk.common',
 'amplitude_python_sdk.common.models',
 'amplitude_python_sdk.common.utils',
 'amplitude_python_sdk.v1',
 'amplitude_python_sdk.v1.models',
 'amplitude_python_sdk.v2',
 'amplitude_python_sdk.v2.models']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8.1,<2.0.0', 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'amplitude-python-sdk',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Krishnan Chandra',
    'author_email': 'krishnan.chandra@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
