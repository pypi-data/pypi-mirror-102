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
    'version': '0.1.1',
    'description': 'Data type for representing time slots with a start and end.',
    'long_description': 'timeslot\n========\n\nClass for working with time slots that have an arbitrary start and end.\n\nCompletes the Python datetime module: datetime (a time), timedelta (a duration), timezone (an offset), **timeslot** (a range/interval).\n\nSupports operations such as: overlaps, intersects, contains, intersection, adjacent, gap, union.\n\nInitially developed as part of [aw-core](https://github.com/ActivityWatch/aw-core), and inspired by a [similar library for .NET](http://www.codeproject.com/Articles/168662/Time-Period-Library-for-NET).\n\nYou might also be interested in [`pandas.Interval`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Interval.html).\n\n\n# Usage\n\nTODO\n\n\n# Synonyms\n\n - timerange (the name was already taken on PyPI)\n - timeperiod (already taken on PyPI)\n - time interval\n',
    'author': 'Erik Bjäreholt',
    'author_email': 'erik@bjareho.lt',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ErikBjare/timeslot',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
