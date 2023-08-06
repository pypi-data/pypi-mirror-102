# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iliad']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'tomlkit>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['iliad = iliad.cli:cli']}

setup_kwargs = {
    'name': 'iliad',
    'version': '0.5.0',
    'description': 'A monorepo tool for Poetry',
    'long_description': '# iliad\nA monorepo tool for [Poetry](https://github.com/python-poetry/poetry)\n\nThe intention is to make a tool that makes working with poetry in monorepos more convenient.\n\n## Install\n```shell\n$ pip install iliad\n```\n\n## Quirks\n- Expects to run within a git repo, uses the `.git` directory to detect the root of the monorepo.\n\n## Usage\n### List\nList the poetry projects detected.\n```shell\n$ iliad list\n//deployment\n//lambdas/alpha\n//lambdas/beta\n//lambdas/delta\n```\n\n### Run\nRuns a command (using `poetry run`) for each of the poetry projects, where the path matches the selector.\n\nPrints out errors for commands that fail.\n```shell\n$ iliad run --selector lambdas -- pytest -v --capture=no\n[done] //lambdas/alpha\n[failed(2)] //lambdas/beta\n[done] //lambdas/delta\n\nfailures:\n[//lambdas/beta] failed with return code 2\n[//lambdas/beta:stdout] ...\n[//lambdas/beta:stderr] ...\n```\n',
    'author': 'Joseph Egan',
    'author_email': 'joseph.s.egan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/eganjs/iliad',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
