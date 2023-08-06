# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['argtyper']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'argtyper',
    'version': '0.1.0',
    'description': 'Argparser on TypeHints and Decorators',
    'long_description': "# ArgTyper\n\n**-- ArgumentParser on Typehints and Decorators**\n\nArgTyper let's you build command line applications from python functions.\nIt is similar to [Typer](https://github.com/tiangolo/typer) (which has more\nfeatures), Contrary to Typer, which is based on [click](https://click.palletsprojects.com/en/7.x/),\nArgTyper is based on standard argparse.ArgumentParser (for better or for\nworse).\n\nYou can find the documentation at https://argtyper.readthedocs.io/\n",
    'author': 'Georg Merzdovnik',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://argtyper.readthedocs.io/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
