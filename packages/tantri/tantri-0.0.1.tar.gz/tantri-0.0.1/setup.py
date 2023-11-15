# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tantri']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.3,<2.0.0', 'scipy>=1.10,<1.11']

setup_kwargs = {
    'name': 'tantri',
    'version': '0.0.1',
    'description': 'Python dipole model evaluator',
    'long_description': '# tantri - generating telegraph noise \n\n',
    'author': 'Deepak',
    'author_email': 'dmallubhotla+github@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<3.10',
}


setup(**setup_kwargs)
