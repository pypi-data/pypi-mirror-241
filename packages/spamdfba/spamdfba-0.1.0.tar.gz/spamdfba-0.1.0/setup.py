# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spamdfba']

package_data = \
{'': ['*']}

install_requires = \
['cobra>=0.27.0,<0.28.0',
 'ipywidgets>=8.1.1,<9.0.0',
 'plotly>=5.17.0,<6.0.0',
 'ray>=2.7.1,<3.0.0',
 'torch>=2.1.0,<3.0.0']

setup_kwargs = {
    'name': 'spamdfba',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'ParsaGhadermazi',
    'author_email': '54489047+ParsaGhadermazi@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
