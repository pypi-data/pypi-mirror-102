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
    'version': '0.1.1',
    'description': 'poetrybot is a Telegram bot to quote poems between friends.',
    'long_description': "poetrybot\n=========\n\npoetrybot is a Telegram bot to quote poems between friends. It's written in\nPython and it is released under the EUPL 1.2 license.\n\nFriends are defined by an allow list in which every account have to be in order\nto to use the bot.\nThe management of the bot is provided by a REST API defined in the subpackage\n``poetrybot.web``.\n\n\nInstallation\n------------\n\n1. Create your bot using Telegram `@BotFather <https://t.me/botfather>`_.\n2. Install (preferably inside a virtualenv) the bot using:\n\n   .. code-block::\n\n      pip install poetrybot\n\n3. The bot uses environment variables as configuration, you have to export the\n   following before starting it:\n\n   .. code-block::\n\n      export AUTH_TOKEN=<my secret auth token>\n      export DATABASE_URL=sqlite:////absolute/path/to/poetrybot.db\n      export TELEGRAM_TOKEN=<telegram bot API key>\n\n   ``AUTH_TOKEN`` is used to authenticate to the REST API used to manage the\n   bot. Full specification is in the ``docs/openapi.yml`` file.\n   Just create a long enough random string, for example using ``pwgen -sy 50``.\n4. Launch the bot:\n\n   .. code-block::\n\n      poetrybot\n5. To use the REST API install a WSGI HTTP Server, for example gunicorn, and\n   then:\n\n   .. code-block::\n\n      gunicorn poetrybot.web.wsgi:app\n\n6. Use the REST API to insert allowed friends, poets and poems. The fastest way\n   to look at the API is to load the API specification into \n   https://editor.swagger.io\n\nAn alternative is to clone the repository and use the provided ``Dockerfile``.\n\nUsage\n-----\n\nTo use the bot you only have to use the ``/quote`` command. The bot can be\nadded to one or more channels but it's not required. But remember that only\nfriends in allow list will be able to interact with the bot.\n\nThe ``/quote`` command used without parameters will make the bot to quote a\nrandom poem, but optionally the author and the argument can be specified:\n\n* ``/quote`` returns a random poem;\n* ``/quote AUTHOR`` returns a random poem by ``AUTHOR``.\n\n  ``AUTHOR`` is the name or part of the name of the poet case insensitive:\n\n  .. code-block::\n\n     /quote Giovanni Pascoli\n     /quote pascoli\n     /quote ascol\n\n  will return a random poem by Giovanni Pascoli, if you don't have another\n  poet with *ascol* inside the name;\n* ``/quote AUTHOR about ARGUMENT`` returns a random poem by ``AUTHOR`` about\n  ``ARGUMENT``.\n\n  ``ARGUMENT`` is, like ``AUTHOR``, case insensitive and can be part of a word.\n  ``about`` is, instead, case sensitive;\n* ``/quote about ARGUMENT`` returns a random poem about ``ARGUMENT``.\n",
    'author': 'Daniele Tricoli',
    'author_email': 'eriol@mornie.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://noa.mornie.org/eriol/poetrybot',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
