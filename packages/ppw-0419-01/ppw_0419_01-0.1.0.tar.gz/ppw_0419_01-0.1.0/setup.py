# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ppw_0419_01', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['fire==0.4.0']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0'],
 'doc': ['mkdocs>=1.1.2,<2.0.0',
         'mkdocs-include-markdown-plugin>=1.0.0,<2.0.0',
         'mkdocs-material>=6.1.7,<7.0.0',
         'mkdocstrings>=0.13.6,<0.14.0',
         'mkdocs-autorefs==0.1.1'],
 'test': ['black==20.8b1',
          'isort==5.6.4',
          'flake8==3.8.4',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest==6.1.2',
          'pytest-cov==2.10.1']}

entry_points = \
{'console_scripts': ['ppw_0419_01 = ppw_0419_01.cli:main']}

setup_kwargs = {
    'name': 'ppw-0419-01',
    'version': '0.1.0',
    'description': 'Skeleton project created by Python Project Wizard (ppw).',
    'long_description': '# ppw 0419 01\n\n\n<p align="center">\n<a href="https://pypi.python.org/pypi/ppw_0419_01">\n    <img src="https://img.shields.io/pypi/v/ppw_0419_01.svg"\n        alt = "Release Status">\n</a>\n\n<a href="https://github.com/zillionare/ppw_0419_01/actions">\n    <img src="https://github.com/zillionare/ppw_0419_01/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">\n</a>\n\n<a href="https://ppw-0419-01.readthedocs.io/en/latest/?badge=latest">\n    <img src="https://readthedocs.org/projects/ppw-0419-01/badge/?version=latest" alt="Documentation Status">\n</a>\n\n</p>\n\n\nSkeleton project created by Python Project Wizard (ppw)\n\n\n* Free software: MIT\n* Documentation: <https://ppw-0419-01.readthedocs.io>\n\n\n## Features\n\n* TODO\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage) project template.\n',
    'author': 'Aaron Yang',
    'author_email': 'code@jieyu.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zillionare/ppw_0419_01',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
