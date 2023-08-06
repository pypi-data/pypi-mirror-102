# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mugmoment']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.17.1,<0.18.0']

setup_kwargs = {
    'name': 'mugmoment',
    'version': '0.1.0',
    'description': 'Library to download chat logs from twitch VODs',
    'long_description': "# mugmoment\n\nmugmoment is a python3 library to download chat logs from twitch VODs.\n\n## Installation\n\n### PyPI\n\nThis package is available on PyPI as `mugmoment`.\n\n### Poetry\n\nThis project uses [poetry](https://python-poetry.org/), and the recommended way of installing it is running `poetry install` on the root of this repository, which will install it in a venv.\n\n## shoutouts\n\n[RechatTool](https://github.com/jdpurcell/RechatTool)'s codebase helped with figuring out how to talk with the API.",
    'author': 'Ave',
    'author_email': 'ave@ave.zone',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/a/mugmoment',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
