# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'plugins'}

packages = \
['tgcf', 'tgcf_filter', 'tgcf_replace']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.1.2,<9.0.0',
 'PyYAML>=5.4.1,<6.0.0',
 'Telethon>=1.20,<2.0',
 'aiohttp>=3.7.4,<4.0.0',
 'cryptg>=0.2.post2,<0.3',
 'hachoir>=3.1.2,<4.0.0',
 'pydantic>=1.8.1,<2.0.0',
 'python-dotenv>=0.15.0,<0.16.0',
 'requests>=2.25.1,<3.0.0',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['tgcf = tgcf:cli.app']}

setup_kwargs = {
    'name': 'tgcf',
    'version': '0.1.15',
    'description': 'The ultimate tool to automate telegram message forwarding.',
    'long_description': '<p align="center">\n<a href = "https://github.com/aahnik/tgcf" > <img src = "https://user-images.githubusercontent.com/66209958/115183360-3fa4d500-a0f9-11eb-9c0f-c5ed03a9ae17.png" alt = "tgcf logo"  width=120> </a>\n</p>\n\n<h1 align="center"> tgcf </h1>\n\n\n<p align="center">\nThe ultimate tool to automate telegram message forwarding.\n</p>\n\n<p align="center"><a href="https://github.com/aahnik/tgcf/blob/main/LICENSE"><img src="https://img.shields.io/github/license/aahnik/tgcf" alt="GitHub license"></a>\n<a href="https://github.com/aahnik/tgcf/stargazers"><img src="https://img.shields.io/github/stars/aahnik/tgcf?style=social" alt="GitHub stars"></a>\n<a href="https://github.com/aahnik/tgcf/issues"><img src="https://img.shields.io/github/issues/aahnik/tgcf" alt="GitHub issues"></a>\n<img src="https://img.shields.io/pypi/v/tgcf" alt="PyPI">\n<a href="https://twitter.com/intent/tweet?text=Wow:&amp;url=https%3A%2F%2Fgithub.com%2Faahnik%2Ftgcf"><img src="https://img.shields.io/twitter/url?style=social&amp;url=https%3A%2F%2Fgithub.com%2Faahnik%2Ftgcf" alt="Twitter"></a></p>\n\n<br>\n\nThe *key features* are:\n\n1. Two [modes of operation](https://github.com/aahnik/tgcf/wiki/Past-vs-Live-modes-explained) are _past_ or _live_ for dealing with either existing or upcoming messages.\n2. Supports [signing in](https://github.com/aahnik/tgcf/wiki/Signing-in-with-a-bot-or-user-account) with both telegram _bot_ account as well as _user_ account.\n3. Custom [Filtering](https://github.com/aahnik/tgcf/wiki/How-to-use-filters-%3F) of messages based on whitelist or blacklist.\n4. Modification of messages like [Text Replacement](https://github.com/aahnik/tgcf/wiki/Text-Replacement-feature-explained), [Watermarking](https://github.com/aahnik/tgcf/wiki/How-to-use--watermarking-%3F), [OCR](https://github.com/aahnik/tgcf/wiki/You-can-do-OCR-!) etc.\n5. Detailed **[documentation📖](https://github.com/aahnik/tgcf/wiki)** + Video tutorial + Fast help in [discussion forum💬](https://github.com/aahnik/tgcf/discussions).\n6. If you are a python developer, writing [plugins🔌](https://github.com/aahnik/tgcf/wiki/How-to-write-a-plugin-for-tgcf-%3F) is like stealing candy from a baby.\n\nWhat are you waiting for? Star 🌟 the repo and click Watch 🕵 to recieve updates.\n\nYou can also join the official [Telegram Channel](https://telegram.me/tg_cf), to recieve updates without any ads.\n\n## Video Tutorial 📺\n\nA youtube video is coming soon. [Subscribe](https://www.youtube.com/channel/UCcEbN0d8iLTB6ZWBE_IDugg) to get notified.\n\n## Run Locally 🔥\n\n> **Note:** Make sure you have Python 3.8 or above installed. Go to [python.org](https://python.org) to download python.\n\n\n\n| Platform | Supported |\n| -------- | :-------: |\n| Windows  |     ✅     |\n| Mac      |     ✅     |\n| Linux    |     ✅     |\n| [Android](https://github.com/aahnik/tgcf/wiki/Run-on-Android-using-Termux)  |     ✅     |\n\nIf you are familiar with **Docker**, you may [go that way](https://github.com/aahnik/tgcf/wiki/Install-and-run-using-docker) for an easier life.\n\nOpen your terminal (command prompt) and run the following commands.\n\n```shell\npip install pipx\npipx install tgcf\n```\n\nTo check if the installation succeeded, run\n\n```shell\ntgcf --version\n```\n\nIf you see an error, that means installation failed.\n\n### Configuration ⚙️\n\nConfiguring `tgcf` is easy. You just need two files.\n\n- [`.env`](https://github.com/aahnik/tgcf/wiki/Environment-Variables) : You heard it right! Just `.env`. This file is for storing your secret credentials for signing into Telegram. This file is for defining the environment variables. You can do so by other methods also.\n\n- [`tgcf.config.yml`](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F) : An `yaml` file to configure how `tgcf` behaves.\n\n\n\n## Run on cloud 🌩️\n\nDeploying to a cloud server is an easier alternative if you cannot install on your own machine. Cloud servers are very reliable and great for running `tgcf` in live mode.\n\nWhen you are deploying on a cloud platform, you can configure `tgcf` using [environment variables](https://github.com/aahnik/tgcf/wiki/Environment-Variables). The contents of [`tgcf.config.yml`]() can be put inside the environment variable called `TGCF_CONFIG`.\n\n\n| How to ?                                                     |\n| :------------------------------------------------------------: |\n| <a href="https://github.com/aahnik/tgcf/wiki/Deploy-to-Heroku">   <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" width=155></a> |\n| <a href="https://github.com/aahnik/tgcf/wiki/Deploy-to-Digital-Ocean">  <img src="https://www.deploytodo.com/do-btn-blue.svg" alt="Deploy to DO" width=220></a> |\n| <a href="https://github.com/aahnik/tgcf/wiki/Run-on-Google-Cloud"> <img src="https://deploy.cloud.run/button.svg" alt="Run on Google Cloud" width=210></a> |\n| <a href="https://github.com/aahnik/tgcf/wiki/Run-for-free-on-Gitpod">  <img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Run on Gitpod" width=160></a> |\n\nIf you need to run `tgcf` in past mode periodically, then you can use [GitHub Actions](https://github.com/aahnik/tgcf/wiki/Run-tgcf-in-past-mode-periodically) to run a scheduled workflow.\n\n\n\n\n## Getting Help 💁🏻\n\n- First of all [read the wiki](https://github.com/aahnik/tgcf/wiki) and [watch the videos.\n- If you still have doubts, you can try searching your problem in discussion forum or the issue tracker.\n- Feel free to ask your questions in the [Discussion forum](https://github.com/aahnik/tgcf/discussions/new).\n- For reporting bugs or requesting a feature please use the [issue tracker](https://github.com/aahnik/tgcf/issues/new) for this repo.\n\nPlease do not send me direct messages in Telegram. (Exception: Sponsors can message me anytime)\n',
    'author': 'aahnik',
    'author_email': 'daw@aahnik.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aahnik/tgcf',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
