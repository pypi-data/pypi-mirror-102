# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dasdo', 'dasdo.utils']

package_data = \
{'': ['*']}

install_requires = \
['Babel>=2.9.0,<3.0.0',
 'pymongo>=3.11.3,<4.0.0',
 'python-telegram-bot>=13.4.1,<14.0.0',
 'sentry-sdk>=1.0.0,<2.0.0']

entry_points = \
{'console_scripts': ['poetry = dasdo']}

setup_kwargs = {
    'name': 'dasdo',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Hadi Zo',
    'author_email': 'hadi.zolfaghaari@gmail.com',
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
