# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['duo_cli']

package_data = \
{'': ['*']}

install_requires = \
['PyInquirer>=1.0.3,<2.0.0',
 'PyNaCl>=1.4.0,<2.0.0',
 'click>=7.1.2,<8.0.0',
 'passlib>=1.7.4,<2.0.0',
 'pyperclip>=1.8.2,<2.0.0',
 'rich>=10.1.0,<11.0.0']

entry_points = \
{'console_scripts': ['duo = duo_cli.cli:main']}

setup_kwargs = {
    'name': 'duo-cli',
    'version': '0.1.0',
    'description': 'Duo Mobile CLI for generating TOTP codes.',
    'long_description': '# Duo CLI\n\nDuo Mobile CLI for generating TOTP codes.\n',
    'author': 'Nathan Cahill',
    'author_email': 'nathan@nathancahill.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nathancahill/duo-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
