# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['consul_docker_autosync']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=1.1.2,<2.0.0',
 'click>=7.1.2,<8.0.0',
 'docker>=5.0.0,<6.0.0',
 'loguru>=0.5.3,<0.6.0',
 'python-consul2>=0.1.5,<0.2.0',
 'waitress>=2.0.0,<3.0.0']

entry_points = \
{'console_scripts': ['cli = consul_docker_autosync.cli:run']}

setup_kwargs = {
    'name': 'consul-docker-autosync',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Dani Hodovic',
    'author_email': 'dani.hodovic@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
