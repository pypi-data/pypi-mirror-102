# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pdf_redactor']
install_requires = \
['defusedxml>=0.7.1,<0.8.0', 'pdfrw>=0.4']

setup_kwargs = {
    'name': 'pdf-redactor',
    'version': '0.0.1',
    'description': 'A general purpose PDF text-layer redaction tool for Python 2/3',
    'long_description': None,
    'author': 'Joshua Tauberer',
    'author_email': 'jt@occams.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
