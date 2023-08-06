# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mail_office',
 'mail_office.management',
 'mail_office.management.commands',
 'mail_office.migrations']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2,<4.0', 'pyfiglet>=0.8.post1,<0.9']

setup_kwargs = {
    'name': 'django-mail-office',
    'version': '0.9.2',
    'description': '',
    'long_description': None,
    'author': 'mikki',
    'author_email': 'mikki@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
