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
    'version': '0.1.2',
    'description': 'Data type for representing time slots with a start and end.',
    'long_description': 'timeslot\n========\n\nClass for working with time slots that have an arbitrary start and end.\n\nCompletes the Python datetime module: datetime (a time), timedelta (a duration), timezone (an offset), **timeslot** (a range/interval).\n\nSupports operations such as: overlaps, intersects, contains, intersection, adjacent, gap, union.\n\nInitially developed as part of [aw-core](https://github.com/ActivityWatch/aw-core), and inspired by a [similar library for .NET](http://www.codeproject.com/Articles/168662/Time-Period-Library-for-NET).\n\nYou might also be interested in [`pandas.Interval`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Interval.html).\n\n\n# Usage\n\n```python\nfrom datetime import datetime, timedelta\nfrom timeslot import Timeslot\n\nnow = datetime.now()\n\nslot = Timeslot(now, now + timedelta(hours=24)\n\nassert slot.duration == timedelta(hours=24)\n\nslot_large = Timeslot(now, now + timedelta(hours=24)\nslot_small = Timeslot(now, now + timedelta(hours=1))\n\n# The events definitely intersect\nassert slot_large.intersects(slot_small)\n\n# The larger even contains the smaller!\nassert slot_large.contains(slot_small)\nassert slot_small in slot_large\n\n# You can also check if a datetime is within the slot\nassert slot_large.contains(now)\n\n# The union of a slot and a contained slot is equal to the larger slot\nassert slot_large == slot_large.union(slot_small)\n\n# Intersection\n# TODO\n\n# Gap\n# TODO\n\n# Adjacent\n# TODO\n```\n\n\n# Synonyms\n\n - timerange (the name was already taken on PyPI)\n - timeperiod (already taken on PyPI)\n - time interval\n',
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
