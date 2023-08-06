# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jarpyvscode',
 'jarpyvscode.projects',
 'jarpyvscode.projects.templates.python',
 'jarpyvscode.projects.templates.python.app',
 'jarpyvscode.projects.templates.python.pkg',
 'jarpyvscode.projects.templates.python.tests',
 'tests']

package_data = \
{'': ['*'], 'jarpyvscode.projects': ['templates/vsce/*']}

setup_kwargs = {
    'name': 'jarpyvscode',
    'version': '0.2.4',
    'description': "Python backend for Jamil Raichouni's personal Visual Studio Code Extension jamilraichouni.jarpyvscode",
    'long_description': None,
    'author': 'Jamil Raichouni',
    'author_email': 'raichouni@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
