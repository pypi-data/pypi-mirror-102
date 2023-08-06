# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetrybot',
 'poetrybot.database',
 'poetrybot.telegram',
 'poetrybot.telegram.commands',
 'poetrybot.web',
 'poetrybot.web.poems',
 'poetrybot.web.poets',
 'poetrybot.web.users']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=1.1.2,<2.0.0',
 'SQLAlchemy>=1.4.3,<2.0.0',
 'environ-config>=20.1.0,<21.0.0',
 'marshmallow>=3.11.1,<4.0.0',
 'python-telegram-bot>=13.4,<14.0']

entry_points = \
{'console_scripts': ['poetrybot = poetrybot.main:main']}

setup_kwargs = {
    'name': 'poetrybot',
    'version': '0.1.0',
    'description': 'poetrybot is a Telegram bot to quote poems between friends.',
    'long_description': None,
    'author': 'Daniele Tricoli',
    'author_email': 'eriol@mornie.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
