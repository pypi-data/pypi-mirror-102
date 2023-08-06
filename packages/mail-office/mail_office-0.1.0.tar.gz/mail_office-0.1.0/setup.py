# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['mail_office']
install_requires = \
['Django>=3.2,<4.0']

setup_kwargs = {
    'name': 'mail-office',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'mikki',
    'author_email': 'mikki@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
