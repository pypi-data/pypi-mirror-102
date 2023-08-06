# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reddit_radio']

package_data = \
{'': ['*'], 'reddit_radio': ['templates/*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'loguru>=0.5.3,<0.6.0',
 'peewee>=3.14.4,<4.0.0',
 'praw>=7.2.0,<8.0.0',
 'python-mpv-jsonipc>=1.1.13,<2.0.0',
 'xdg>=5.0.1,<6.0.0']

entry_points = \
{'console_scripts': ['reddit_radio = reddit_radio.cli:cli']}

setup_kwargs = {
    'name': 'reddit-radio',
    'version': '0.0.2',
    'description': 'Listen to music shared on reddit from your command line',
    'long_description': '# Reddit radio\n\n![workflow](https://github.com/martini97/reddit_radio/actions/workflows/ci.yaml/badge.svg)\n[![codecov](https://codecov.io/gh/martini97/reddit_radio/branch/main/graph/badge.svg)](https://codecov.io/gh/martini97/reddit_radio)\n[![CodeQL](https://github.com/martini97/reddit_radio/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/martini97/reddit_radio/actions?query=workflow%3ACodeQL)\n[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)\n\n## Install\n\n```bash\npip install reddit-radio\n```\n\n## Config\n\nBefore running you need to setup the config file, there is a sample in\n`config.sample.ini` for your client\\_id and client\\_secret you need to go to this\nurl: https://www.reddit.com/prefs/apps and create a new app. Then move the file to\n`~/.config/reddit_radio.ini`.\n\n## Usage\n\n```sh\npython -m reddit_radio load-data play\n```\n\n## Dependencies\n\n+ [MPV](https://mpv.io/)\n',
    'author': 'martini97',
    'author_email': 'martini97@protonmail.ch',
    'maintainer': 'martini97',
    'maintainer_email': 'martini97@protonmail.ch',
    'url': 'https://github.com/martini97/reddit_radio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
