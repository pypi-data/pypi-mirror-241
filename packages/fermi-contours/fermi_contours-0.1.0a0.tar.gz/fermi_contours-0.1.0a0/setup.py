# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fermi_contours']

package_data = \
{'': ['*']}

install_requires = \
['certifi>=2023.07.22,<2024.0.0',
 'click>=8.0.1',
 'dparse>=0.6.2,<0.7.0',
 'gitpython>=3.1.35,<4.0.0',
 'ipython>=8.10.0,<9.0.0',
 'markdown-it-py>=2.2.0,<3.0.0',
 'numpy>=1.23.5,<2.0.0',
 'pygments>=2.15.0,<3.0.0',
 'requests>=2.31.0,<3.0.0',
 'tornado>=6.3.2,<7.0.0',
 'urllib3>=1.26.17,<2.0.0']

entry_points = \
{'console_scripts': ['fermi-contours = fermi_contours.__main__:main']}

setup_kwargs = {
    'name': 'fermi-contours',
    'version': '0.1.0a0',
    'description': 'Fermi Contours',
    'long_description': "# Fermi Contours\n\n[![PyPI](https://img.shields.io/pypi/v/fermi-contours.svg)][pypi status]\n[![Status](https://img.shields.io/pypi/status/fermi-contours.svg)][pypi status]\n[![Python Version](https://img.shields.io/pypi/pyversions/fermi-contours)][pypi status]\n[![License](https://img.shields.io/pypi/l/fermi-contours)][license]\n\n[![Read the documentation at https://fermi-contours.readthedocs.io/](https://img.shields.io/readthedocs/fermi-contours/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/piskunow/fermi-contours/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/piskunow/fermi-contours/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi status]: https://pypi.org/project/fermi-contours/\n[read the docs]: https://fermi-contours.readthedocs.io/\n[tests]: https://github.com/piskunow/fermi-contours/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/piskunow/fermi-contours\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- TODO\n\n## Requirements\n\n- TODO\n\n## Installation\n\nYou can install _Fermi Contours_ via [pip] from [PyPI]:\n\n```console\n$ pip install fermi-contours\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Fermi Contours_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/piskunow/fermi-contours/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/piskunow/fermi-contours/blob/main/LICENSE\n[contributor guide]: https://github.com/piskunow/fermi-contours/blob/main/CONTRIBUTING.md\n[command-line reference]: https://fermi-contours.readthedocs.io/en/latest/usage.html\n",
    'author': 'Pablo Piskunow',
    'author_email': 'pablo.perez.piskunow@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/piskunow/fermi-contours',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
