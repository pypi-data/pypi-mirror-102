# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sprite_unpack']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.2.0,<9.0.0', 'tqdm>=4.60.0,<5.0.0']

entry_points = \
{'console_scripts': ['sprite-unpack = sprite_unpack.cli:main']}

setup_kwargs = {
    'name': 'sprite-unpack',
    'version': '0.1.0',
    'description': 'Tool for cutting spritesheets into seperate images for importing into Godot, Unity, etc.',
    'long_description': '',
    'author': 'Ilya Averyanov',
    'author_email': 'av@rubybox.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/savonarola/sprite_unpack',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
