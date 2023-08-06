# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['txt_hours']
install_requires = \
['pandas==1.1.5']

entry_points = \
{'console_scripts': ['txthours = txt_hours:main']}

setup_kwargs = {
    'name': 'txt-hours',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Andrew Simmons',
    'author_email': 'agsimmons0@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
