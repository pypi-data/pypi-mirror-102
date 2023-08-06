# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dupe']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dupe',
    'version': '0.0.2',
    'description': 'Find duplicate files',
    'long_description': None,
    'author': 'Damon Allison',
    'author_email': 'damon@damonallison.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
