# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eox_notices',
 'eox_notices.api',
 'eox_notices.migrations',
 'eox_notices.tests']

package_data = \
{'': ['*'],
 'eox_notices': ['templates/eox_notices/*', 'templates/eox_notices/inc/*']}

setup_kwargs = {
    'name': 'nautobot-eox-notices',
    'version': '0.1.0',
    'description': 'Tracks EoX Notices for Nautobot objects.',
    'long_description': '# nautobot-eox-notices\n\nA plugin for [Nautobot](https://github.com/nautobot/nautobot).\n\n## Installation\n\nThe plugin is available as a Python package in pypi and can be installed with pip\n\n```shell\npip install nautobot-eox-notices\n```\n\n> The plugin is compatible with Nautobot 1.0.0b1 and higher\n\nTo ensure Nautobot EoX Tracker is automatically re-installed during future upgrades, create a file named `local_requirements.txt` (if not already existing) in the Nautobot root directory (alongside `requirements.txt`) and list the `nautobot-eox-notices` package:\n\n```no-highlight\n# echo nautobot-eox-notices >> local_requirements.txt\n```\n\nOnce installed, the plugin needs to be enabled in your `configuration.py`\n\n```python\n# In your configuration.py\nPLUGINS = ["eox_notices"]\n\n# PLUGINS_CONFIG = {\n#   "eox_notices": {\n#     ADD YOUR SETTINGS HERE\n#   }\n# }\n```\n\nThe plugin behavior can be controlled with the following list of settings\n\n- TODO\n\n## Usage\n\n### API\n\nTODO\n\n## Contributing\n\nPull requests are welcomed and automatically built and tested against multiple version of Python and multiple version of Nautobot through TravisCI.\n\nThe project is packaged with a light development environment based on `docker-compose` to help with the local development of the project and to run the tests within TravisCI.\n\nThe project is following Network to Code software development guideline and is leveraging:\n\n- Black, Pylint, Bandit and pydocstyle for Python linting and formatting.\n- Django unit test to ensure the plugin is working properly.\n\n### CLI Helper Commands\n\nThe project is coming with a CLI helper based on [invoke](http://www.pyinvoke.org/) to help setup the development environment. The commands are listed below in 3 categories `dev environment`, `utility` and `testing`. \n\nEach command can be executed with `invoke <command>`. All commands support the arguments `--nautobot-ver` and `--python-ver` if you want to manually define the version of Python and Nautobot to use. Each command also has its own help `invoke <command> --help`\n\n#### Local dev environment\n\n```no-highlight\n  build            Build all docker images.\n  debug            Start Nautobot and its dependencies in debug mode.\n  destroy          Destroy all containers and volumes.\n  restart          Restart Nautobot and its dependencies.\n  start            Start Nautobot and its dependencies in detached mode.\n  stop             Stop Nautobot and its dependencies.\n```\n\n#### Utility\n\n```no-highlight\n  cli              Launch a bash shell inside the running Nautobot container.\n  create-user      Create a new user in django (default: admin), will prompt for password.\n  makemigrations   Run Make Migration in Django.\n  nbshell          Launch a nbshell session.\n```\n\n#### Testing\n\n```no-highlight\n  bandit           Run bandit to validate basic static code security analysis.\n  black            Run black to check that Python files adhere to its style standards.\n  flake8           This will run flake8 for the specified name and Python version.\n  pydocstyle       Run pydocstyle to validate docstring formatting adheres to NTC defined standards.\n  pylint           Run pylint code analysis.\n  tests            Run all tests for this plugin.\n  unittest         Run Django unit tests for the plugin.\n```\n\n## Screenshots\n\nTODO\n',
    'author': 'Mikhail Yohman',
    'author_email': 'mikhail.yohman@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fragmentedpacket/nautobot-eox-notices',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
