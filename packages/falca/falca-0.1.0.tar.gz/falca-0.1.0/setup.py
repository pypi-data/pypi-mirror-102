# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['falca']

package_data = \
{'': ['*']}

install_requires = \
['falcon>=3.0.0,<4.0.0']

setup_kwargs = {
    'name': 'falca',
    'version': '0.1.0',
    'description': 'wip',
    'long_description': None,
    'author': 'aprilahijriyan',
    'author_email': 'hijriyan23@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
