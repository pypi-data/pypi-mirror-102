# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['envcon', 'envcon.utils']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.17.0,<0.18.0']

setup_kwargs = {
    'name': 'envcon',
    'version': '0.1.6',
    'description': '',
    'long_description': '# envcon: easy environment variables parsing\n\n\n**Envcon** -  easy environment variables parsing.\nEnvcon allows you to store configuration separated from your code, like \n[The Twelve-Factor App](https://12factor.net/config) suggests.  \nEnvcon heavily leaned on python type-hints and makes configuration simple and declerative. \n\n## Contents\n\n- [Features](#features)\n- [Install](#install)\n- [Usage](#usage)\n  - [Basic usage](#basic-usage)\n  - [Prefix](#prefix)\n- [Supported types](#supported-types)\n- [Reading .env files](#reading-env-files)\n- [Why...?](#why)\n  - [Why environment variables?](#why-environment-variables)\n  - [Why not os.environ?](#why-not-osenviron)\n- [License](#license)\n\n## Features\n\n- Simple usage\n- Type-casting\n- Parse `.env` files as well as environment variables (`os.environ`) (useful for development)\n- Default values\n- Prefix\n\n## Install\n\n    pip install envcon\n\n## Usage\n\nAssuming these environment variables are set (or written in .env file)\n\n```bash\nexport MONGO_USER=myMongoUser\nexport MONGO_PASSWORD=shh_its_a_secret\nexport SECRET_NUMBER=0.42\nexport ONE_TO_TEN=1,2,3,4,5,6,7,8,9,10\nexport IS_ENABLED=true\nexport URL=http://www.google.com\n```\n\n### Basic usage\n\n```python3\nfrom envcon import environment_configuration\n\n@environment_configuration\nclass Configs:\n    SECRET_NUMBER: float\n    IS_ENABLED: bool\n    ONE_TO_TEN: list[int] # on python 3.8 use List[int] (from typing import List) \n\nprint(Configs.SECRET_NUMBER) # 0,42\nprint(type(Configs.SECRET_NUMBER)) # <class \'float\'>\nprint(Configs.IS_ENABLED) # True\nprint(type(Configs.IS_ENABLED)) # <class \'bool\'>\nprint(type(Configs.ONE_TO_TEN[0])) # <class \'int\'> \n```\n\n### Prefix\n\n```python3\nfrom envcon import environment_configuration\n\n@environment_configuration(prefix="MONGO_")\nclass MongoConfiguration:\n    USER: str\n    PASSWORD: str\n\nprint(MongoConfiguration.USER) # myMongoUser\n    \n```\n\n## Supported types\n\nThe following types hints are supported\n\nBuiltins and from `typing`:\n- `str`\n- `bool`\n- `int`\n- `float`\n- `list`\n- `list[T]` # >= python 3.9\n- `dict` \n- `List`\n- `List[T]`\n- `Dict`\n- `Optional[T]`\n\n## Reading `.env` files\nBy default, envcon will parse your `.env` file.\nThis feature is useful for local development.  \nnotice that .env will not override your environment variables.  \n\nYou can turn this feature off:  \n```python3\n@environment_configuration(include_dot_env_file=False)\nclass MyConfigClass:\n    ...\n```\n\n\n## Why...?\n\n### Why environment variables?\n\nSee [The 12-factor App](http://12factor.net/config) section on\n[configuration](http://12factor.net/config).\n\n### Why not `os.environ`?\nBasically, because this:\n```python3\nclass Config:\n    MAX_CONNECTION = int(os.environ.get("MAX_CONNECTION", "42"))\n    TIMEOUT = float(os.environ.get("TIMEOUT", "4.2"))\n    MY_PASSWORD = os.environ["MY_PASSWORD"] #required w/o default value\n    OPTIONAL_URL = os.environ.get("OPTIONAL_URL", None)\n    OPTIONAL_NUMBER = int(os.environ.get("OPTIONAL_NUMBER", "0")) or None\n    NUMS_LIST = [int(i) for i in os.environ["NUMS_LIST"].splite(",")]\n    NUMS_LIST_WITH_DEFAULT = [int(i) for i in os.environ.get("NUMS_LIST", "1,2,3").splite(",")]\n```\n\nwill simply turn into this:\n```python3\nfrom typing import Optional, List\n\n@environment_configuration\nclass Config:\n    MAX_CONNECTION: int = 42\n    TIMEOUT: float = 4.2\n    MY_PASSWORD: str\n    OPTIONAL_URL: Optional[str]\n    OPTIONAL_NUMBER: Optional[int]\n    NUMS_LIST: list[int] # in python 3.8 use List[int]\n    NUMS_LIST_WITH_DEFAULT: list[int] = [1, 2, 3]\n```\n\nenvcon will help you\n\n- cast environment variables to the correct type\n- specify required environment variables\n- define default values\n- parse list and dict\n\n## License\n\nMIT licensed.  ',
    'author': 'Neria',
    'author_email': 'me@neria.dev',
    'maintainer': 'Neria',
    'maintainer_email': 'me@neria.dev',
    'url': 'https://github.com/neriat/envcon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
