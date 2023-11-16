# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fut_listen']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.7,<9.0.0']

entry_points = \
{'console_scripts': ['fut-listen = fut_listen.cli:cli']}

setup_kwargs = {
    'name': 'fut-listen',
    'version': '0.2.0',
    'description': 'CLI Program to automate listening sections for tests.',
    'long_description': "# FUT-LISTEN\n\n```\n  /`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`\n  /`     ┏━╸╻ ╻╺┳╸   ╻  ╻┏━┓╺┳╸┏━╸┏┓╻     /`\n  /`     ┣╸ ┃ ┃ ┃ ╺━╸┃  ┃┗━┓ ┃ ┣╸ ┃┗┫     /`\n  /`     ╹  ┗━┛ ╹    ┗━╸╹┗━┛ ╹ ┗━╸╹ ╹     /`\n  /`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`/`\n```\n\nA CLI Program to automate listening sections for tests.\n\n### What it does\n\nThe default behavior is to search through the current working directory for *.mp3 files. It will sort the files in order, and then play them twice. There are instructions given (with TTS) and delays given throughout, with tones to indicate that the next portion will happen soon. It's basically an automated playlist.\n\nThe defaults probably work fine, but there are a lot of options. \n\nThis program doesn't do any trimming of audio. If you need to do that, use another tool. \n\n### Requirements:\n\n1. You should have a high-quality TTS voice downloaded. [Read here](https://support.apple.com/guide/mac-help/change-the-voice-your-mac-uses-to-speak-text-mchlp2290/mac) to find out more.\n2. [mpv](https://mpv.io) is used for playing audio. Install it using homebrew: `brew install mpv`.\n3. [sox](https://sourceforge.net/projects/sox/) is used to play tones. Install it using homebrew: `brew install sox`.\n\n### Installation\n\nIt's best to use [pipx](https://pypa.github.io/pipx/):\n\n```\npipx install fut-listen\n```\n\nAlternatively, install with pip:\n\n```\npip install fut-listen\n```\n\n### Usage\n\n```\n# navigate to directory\nfut-listen\n\n# See options\nfut-listen --help\n```\n",
    'author': 'Dan Cook',
    'author_email': 'cook.r.dan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
