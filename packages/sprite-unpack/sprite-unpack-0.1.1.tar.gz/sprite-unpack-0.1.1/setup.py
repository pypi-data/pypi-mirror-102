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
    'version': '0.1.1',
    'description': 'Tool for cutting spritesheets into seperate images for importing into Godot, Unity, etc.',
    'long_description': '# Sprite unpack\n\n[![CI](https://github.com/savonarola/sprite_unpack/actions/workflows/CI.yml/badge.svg)](https://github.com/savonarola/sprite_unpack/actions/workflows/CI.yml)\n\n## Description\n\nUtility script for cutting sprite sheets into sprite images. See examples section.\n\n## Installation\n\n```bash\npip install sprite-unpack\n```\n\n## Requirements\n\nPython >= 3.9\n\n## Usage\n\n```bash\nsprite-unpack -i examples/doctor-doom-sheet.png -o ./examples/result\n```\n\n## Example\n\nI am fan of writing tiny games. Usually I use free sprite sheets for them.\nThis script cuts sprite sheets into separate images ready for use in\nGodot, Unity, etc.\n\nThe result of cutting [doctor-doom-sheet.png](examples/doctor-doom-sheet.png)\ninto images can be found in [examples/result](examples/result) folder.\n\nThe algorithm is pretty straigtforward and can be easily\nunderstood from the following recording:\n\n![Algo](examples/doctor-doom-sprites.gif).\n\n**Caution!** The script does not handle disjoint sprites with many particles.\n',
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
