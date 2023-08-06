# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['beanie',
 'beanie.executors',
 'beanie.migrations',
 'beanie.migrations.controllers',
 'beanie.odm']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'motor>=2.1.0,<3.0.0',
 'pydantic>=1.8,<2.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['beanie = beanie.executors.migrate:migrations']}

setup_kwargs = {
    'name': 'beanie',
    'version': '0.4.0',
    'description': 'Asynchronous Python ODM for MongoDB',
    'long_description': '![Beanie](https://raw.githubusercontent.com/roman-right/beanie/main/assets/logo/with_text.svg)\n\n[Beanie](https://github.com/roman-right/beanie) - is an asynchronous ODM for MongoDB, based on [Motor](https://motor.readthedocs.io/en/stable/)\nand [Pydantic](https://pydantic-docs.helpmanual.io/).\n\nIt uses an abstraction over Pydantic models and Motor collections to work with the database. Class Document allows to\ncreate, replace, update, get, find and aggregate.\n\nBeanie supports migrations out of the box.\n\n### Installation\n\n#### PIP\n\n```shell\npip install beanie\n```\n\n#### Poetry\n\n```shell\npoetry add beanie\n```\n\n### Quick Start\n\n```python\nfrom typing import Optional, List\n\nimport motor\nfrom beanie import Document, init_beanie\nfrom pydantic import BaseModel\n\n\nclass Tag(BaseModel):\n    name: str\n    color: str\n\n\nclass Note(Document):\n    title: str\n    text: Optional[str]\n    tag_list: List[Tag] = []\n\n\nasync def main():\n    client = motor.motor_asyncio.AsyncIOMotorClient(\n        "mongodb://user:pass@host:27017"\n    )\n    await init_beanie(database=client.db_name, document_models=[Note])\n\n    all_notes = await Note.find_all().to_list()\n```\n\n### Materials\n\n#### ODM\n- **[Tutorial](https://roman-right.github.io/beanie/tutorial/odm/)** - ODM usage examples\n- **[Documentation](https://roman-right.github.io/beanie/documentation/odm/)** - Full list of the ODM classes and\n  methods with descriptions\n\n#### Migrations\n- **[Tutorial](https://roman-right.github.io/beanie/tutorial/odm/)** - Migrations usage examples\n\n### Resources\n\n- **[GitHub](https://github.com/roman-right/beanie)** - GitHub page of the project\n- **[Changelog](https://roman-right.github.io/beanie/changelog)** - list of all the valuable changes\n- **[Discord](https://discord.gg/ZTTnM7rMaz)** - ask your questions, share ideas or just say `Hello!!`\n\n### Articles\n\n- [Announcing Beanie - MongoDB ODM](https://dev.to/romanright/announcing-beanie-mongodb-odm-56e)\n- [Build a Cocktail API with Beanie and MongoDB](https://developer.mongodb.com/article/beanie-odm-fastapi-cocktails/)\n- [MongoDB indexes with Beanie](https://dev.to/romanright/mongodb-indexes-with-beanie-43e8)',
    'author': 'Roman',
    'author_email': 'roman-right@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/roman-right/beanie',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
