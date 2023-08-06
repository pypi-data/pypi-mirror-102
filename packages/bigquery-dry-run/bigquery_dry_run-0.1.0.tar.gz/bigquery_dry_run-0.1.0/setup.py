# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bigquery_dry_run']

package_data = \
{'': ['*']}

install_requires = \
['google-cloud-bigquery>=2.13.1,<3.0.0']

entry_points = \
{'console_scripts': ['bqdry = bigquery_dry_run.app:run']}

setup_kwargs = {
    'name': 'bigquery-dry-run',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Christo Olivier',
    'author_email': 'mail@christoolivier.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<3.10',
}


setup(**setup_kwargs)
