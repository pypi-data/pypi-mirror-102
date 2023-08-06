# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['triehard', 'triehard.lib']

package_data = \
{'': ['*']}

install_requires = \
['python-nubia>=0.2b5,<0.3',
 'requests>=2.25.1,<3.0.0',
 'termcolor>=1.1.0,<2.0.0']

entry_points = \
{'console_scripts': ['trie = cli:main']}

setup_kwargs = {
    'name': 'triehard',
    'version': '0.1.7',
    'description': 'A badly implemented trie',
    'long_description': None,
    'author': 'iCalculated',
    'author_email': 'fufa0001@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
