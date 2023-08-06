# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['af_ibov_downloader']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['af-ibov-downloader = af_ibov_downloader.cli:main']}

setup_kwargs = {
    'name': 'af-ibov-downloader',
    'version': '0.1.0',
    'description': 'A CLI tool to download market data from ibovespa',
    'long_description': '# Aerfin Ibov Downloaders\n\nA CLI that downloads archives from the ibovespa website.\n\n## Requirements\n\n* python >= 3.6\n* asyncio\n* typing (type hints)\n\n## Installation\n\nIntalling from gitlab:\n\n```bash\npip install -u git+https://gitlab.com/aerofin/tooling/af-ibov-downloader.git@master\n```\n\nInstalling from pypi:\n\n```bash\npip install -u af-ibov-downloader\n```\n\n## Usage\n\nOnce installed, the CLi will be available as `af-ibov-downloader`.\n\nRun `af-ibov-downloader --help` for commands or check the [docs website](https://af-ibov-archive.readthedocs.org).\n\n## Development\n\nA `Makefile` is provided for common tasks, such as running tests.\n\nThe project uses poetry ad "project tooling" but `requirements` files for both prod and dev are provided for convenience.\n\nA `setup.py` file is generated using `dephell`.\n\nTests are based on `pytest` but they can be used by running `make test`.\n\nThe project also depends on `mypy` in strict mode which is used before running the actual tests.\n\n## License\n\nMIT\n',
    'author': 'Leonardo Rossetti',
    'author_email': 'me@lrossetti.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://af-ibov-downloader.readthedocs.io/en/latest/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
