# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['timeslot']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'timeslot',
    'version': '0.1.0',
    'description': 'Data type for representing time slots with a start and end.',
    'long_description': None,
    'author': 'Erik Bjäreholt',
    'author_email': 'erik@bjareho.lt',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
