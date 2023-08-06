# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['texto', 'texto.algorithms', 'texto.utils']

package_data = \
{'': ['*'], 'texto': ['cache/*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'gensim==4.0.0b0',
 'matplotlib==3.3.4',
 'nltk==3.5',
 'spacy==3.0.3']

entry_points = \
{'console_scripts': ['texto = texto.entry:cli']}

setup_kwargs = {
    'name': 'texto',
    'version': '0.1.2',
    'description': 'Projet de textométrie.',
    'long_description': None,
    'author': 'Jérémy DEMANGE',
    'author_email': 'jeremy@scrapfast.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
