# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kedro_hyperparam']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0']

entry_points = \
{'console_scripts': ['kedro-hyperparam = kedro_hyperparam.__main__:main']}

setup_kwargs = {
    'name': 'kedro-hyperparam',
    'version': '0.0.1a0',
    'description': 'Kedro Hyperparam',
    'long_description': "Kedro Hyperparam\n================\n\n|PyPI| |Python Version| |License|\n\n|Read the Docs| |Tests| |Codecov|\n\n|pre-commit| |Black|\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/kedro-hyperparam.svg\n   :target: https://pypi.org/project/kedro-hyperparam/\n   :alt: PyPI\n.. |Python Version| image:: https://img.shields.io/pypi/pyversions/kedro-hyperparam\n   :target: https://pypi.org/project/kedro-hyperparam\n   :alt: Python Version\n.. |License| image:: https://img.shields.io/pypi/l/kedro-hyperparam\n   :target: https://opensource.org/licenses/MIT\n   :alt: License\n.. |Read the Docs| image:: https://img.shields.io/readthedocs/kedro-hyperparam/latest.svg?label=Read%20the%20Docs\n   :target: https://kedro-hyperparam.readthedocs.io/\n   :alt: Read the documentation at https://kedro-hyperparam.readthedocs.io/\n.. |Tests| image:: https://github.com/stasulam/kedro-hyperparam/workflows/Tests/badge.svg\n   :target: https://github.com/stasulam/kedro-hyperparam/actions?workflow=Tests\n   :alt: Tests\n.. |Codecov| image:: https://codecov.io/gh/stasulam/kedro-hyperparam/branch/main/graph/badge.svg\n   :target: https://codecov.io/gh/stasulam/kedro-hyperparam\n   :alt: Codecov\n.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white\n   :target: https://github.com/pre-commit/pre-commit\n   :alt: pre-commit\n.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n   :alt: Black\n\n\nFeatures\n--------\n\n* TODO\n\n\nRequirements\n------------\n\n* TODO\n\n\nInstallation\n------------\n\nYou can install *Kedro Hyperparam* via pip_ from PyPI_:\n\n.. code:: console\n\n   $ pip install kedro-hyperparam\n\n\nUsage\n-----\n\nPlease see the `Command-line Reference <Usage_>`_ for details.\n\n\nContributing\n------------\n\nContributions are very welcome.\nTo learn more, see the `Contributor Guide`_.\n\n\nLicense\n-------\n\nDistributed under the terms of the `MIT license`_,\n*Kedro Hyperparam* is free and open source software.\n\n\nIssues\n------\n\nIf you encounter any problems,\nplease `file an issue`_ along with a detailed description.\n\n\nCredits\n-------\n\nThis project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.\n\n.. _@cjolowicz: https://github.com/cjolowicz\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _MIT license: https://opensource.org/licenses/MIT\n.. _PyPI: https://pypi.org/\n.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n.. _file an issue: https://github.com/stasulam/kedro-hyperparam/issues\n.. _pip: https://pip.pypa.io/\n.. github-only\n.. _Contributor Guide: CONTRIBUTING.rst\n.. _Usage: https://kedro-hyperparam.readthedocs.io/en/latest/usage.html\n",
    'author': 'Lukasz Ambroziak',
    'author_email': 'l.ambroziak@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/stasulam/kedro-hyperparam',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
