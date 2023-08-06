# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['doma', 'doma.migrations', 'doma.tests']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2,<4.0', 'Pillow>=8.2.0,<9.0.0']

setup_kwargs = {
    'name': 'django-doma',
    'version': '0.1.0',
    'description': 'Simple Document Management for Django',
    'long_description': None,
    'author': 'Florian Rämisch',
    'author_email': 'olf@subsignal.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
