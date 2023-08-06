# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pseudonymize_pdf']
install_requires = \
['pdf-redactor>=0.0.1,<0.0.2']

setup_kwargs = {
    'name': 'pseudonymize-pdf',
    'version': '0.3.0',
    'description': 'A convenience library to read and alter PDFs to remove personally identifying data',
    'long_description': '# Pseudonymize PDF\nA convenience library to read and alter PDFs to remove personally identifying data.\n',
    'author': 'Stephen Badger',
    'author_email': 'stephen.badger@vitalbeats.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vitalbeats/pseudonymize-pdf',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
