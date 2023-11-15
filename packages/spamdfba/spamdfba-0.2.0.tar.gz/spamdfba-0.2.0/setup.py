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
    'version': '0.2.0',
    'description': '',
    'long_description': '# SPAM-DFBA Documentation Website\n\nParsa Ghadermazi: Parsa.ghadermazi@colostate.edu\n\n# SPAM-DFBA\n\n## Introduction\n\nSPM-DFBA is an algoritm for inferring microbial interactions by modeling microbial metabolism in a community as a decision making process, a markov decision process more specifically, where individual agents learn metabolic regulation strategies that lead to their long-term survival by trying different strategies and improve their strategies according to proximal policy optimization algorithm.\n\n***More information can be found in the documentation website for this project:***\n\nhttps://chan-csu.github.io/SPAM-DFBA/\n\n## Installation\n\nThere are multiple ways to install SPAM-DFBA. Before doing any installation it is highly recomended that you create a new environment for this project.\nAfter creating the virtual environment and activating it, one way for installation is to clone the ripository and pip install from the source files:\n\n```\n\ngit clone https://github.com/chan-csu/SPAM-DFBA.git\ncd SPAM-DFBA\npip install .\n\n```\nAnother approach is to directly install this package from pipy:\n\n```\npip install spamdfba\n```\n\n## Examples\n\nThe examples used in the manuscript are provided in separated jupyter notebooks in the ./examples directory. Additionally, they are provided in the documentation website for this project under Case Study-* section\n\nDuring training, different objects are saved into pickle files whick are also provided in ./examples/Results/ for each environment.\n\n## Contribution\n\nIf you have any suggestions or issues related to this project please open an issue or suggest a pull request for further imrovements!\n\n\n\n\n\n\n\n',
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
