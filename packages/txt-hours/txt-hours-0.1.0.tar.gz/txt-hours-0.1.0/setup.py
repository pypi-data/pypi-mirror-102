# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['txt_hours']
entry_points = \
{'console_scripts': ['txthours = txt_hours:_main']}

setup_kwargs = {
    'name': 'txt-hours',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Andrew Simmons',
    'author_email': 'agsimmons0@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
