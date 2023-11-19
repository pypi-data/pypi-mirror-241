# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['emblematic']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.2,<5.0.0',
 'cairosvg>=2.6.0,<3.0.0',
 'click>=8.1.3,<9.0.0',
 'lxml>=4.9.2,<5.0.0']

extras_require = \
{'docs': ['Sphinx>=7.2.6,<8.0.0', 'sphinx-rtd-theme>=1.2.0,<2.0.0']}

entry_points = \
{'console_scripts': ['emblematic = emblematic.__main__:main']}

setup_kwargs = {
    'name': 'emblematic',
    'version': '1.0.4',
    'description': 'Generate emblems from an icon and a background',
    'long_description': '# ![](media/icon-round-100x100.png) Emblematic\n\nGenerate emblems from an icon and a background\n\n## Links\n\n[![PyPI](https://img.shields.io/pypi/v/emblematic)](https://pypi.org/project/emblematic)\n\u2002\n[![Documentation](https://img.shields.io/readthedocs/emblematic\n)](https://emblematic.readthedocs.io/latest/)\n',
    'author': 'Stefano Pigozzi',
    'author_email': 'me@steffo.eu',
    'maintainer': 'Stefano Pigozzi',
    'maintainer_email': 'me@steffo.eu',
    'url': 'https://github.com/Steffo99/emblematic/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
