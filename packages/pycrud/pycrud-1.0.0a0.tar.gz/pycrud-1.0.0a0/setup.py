# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycrud',
 'pycrud.crud',
 'pycrud.crud.ext',
 'pycrud.helpers',
 'pycrud.helpers.fastapi_ext',
 'pycrud.helpers.pydantic_ext',
 'pycrud.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyPika>=0.42.1',
 'multidict>=4.5,<6.0',
 'pydantic>=1.6.1',
 'typing_extensions>=3.7.4.2']

setup_kwargs = {
    'name': 'pycrud',
    'version': '1.0.0a0',
    'description': 'A common crud framework for web.',
    'long_description': '# pycrud\n\n[![codecov](https://codecov.io/gh/fy0/pycrud/branch/master/graph/badge.svg)](https://codecov.io/gh/fy0/pycrud)\n\nAn async crud framework for RESTful API.\n\nFeatures:\n\n* Do CRUD operations by json.\n\n* Easy to integrate with web framework.\n\n* Works with popular orm.\n\n* Role based permission system\n\n* Data validate with pydantic.\n\n* Tested coveraged\n\n### Install:\n\n```bash\npip install pycrud==1.0.0a0\n```\n\n### Examples:\n\n#### CRUD service by fastapi and SQLAlchemy\n\n```python\nfrom typing import Optional\n\nimport uvicorn\nfrom fastapi import FastAPI, Request\nfrom fastapi.middleware.cors import CORSMiddleware\n\nfrom sqlalchemy import create_engine\nfrom sqlalchemy.orm import declarative_base, sessionmaker\nfrom sqlalchemy import Column, Integer, String, Sequence\n\nfrom pycrud.crud.ext.sqlalchemy_crud import SQLAlchemyCrud\nfrom pycrud.helpers.fastapi_ext import QueryDto\nfrom pycrud.query import QueryInfo\nfrom pycrud.types import Entity\nfrom pycrud.values import ValuesToUpdate\n\n\n# ORM Initialize\n\nengine = create_engine("sqlite:///:memory:")\nBase = declarative_base()\nSession = sessionmaker(bind=engine)\n\n\nclass UserModel(Base):\n    __tablename__ = \'users\'\n    id = Column(Integer, Sequence(\'user_id_seq\'), primary_key=True)\n    nickname = Column(String)\n    username = Column(String)\n    password = Column(String, default=\'password\')\n    update_test: Column(String, default=\'update\')\n\n\nBase.metadata.create_all(engine)\n\nsession = Session()\nsession.add_all([\n    UserModel(nickname=\'a\', username=\'a1\'),\n    UserModel(nickname=\'b\', username=\'b2\'),\n    UserModel(nickname=\'c\', username=\'c3\')\n])\nsession.commit()\n\n\n# Crud Initialize\n\nclass User(Entity):\n    id: Optional[int]\n    nickname: str\n    username: str\n    password: str = \'password\'\n\n\nc = SQLAlchemyCrud(None, {\n    User: \'users\'\n}, engine)\n\n\n# Web Service\n\napp = FastAPI()\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=[\'*\'],\n    allow_credentials=True,\n    allow_methods=["*"],\n    allow_headers=["*"],\n)\n\n\n@app.post("/user/create")\nasync def user_create(item: User.dto.get_create()):\n    return await c.insert_many(User, [item])  # response id list: [1]\n\n\n@app.get("/user/list")\nasync def user_list(query_json=QueryDto(User)):\n    q = QueryInfo.from_json(User, query_json)\n    return [x.to_dict() for x in await c.get_list(q)]\n\n\n@app.post("/user/update")\nasync def user_list(item: User.dto.get_update(), query_json=QueryDto(User)):\n    q = QueryInfo.from_json(User, query_json)\n    return await c.update(q, ValuesToUpdate(item))\n\n\n@app.post("/user/delete")\nasync def user_delete(query_json=QueryDto(User)):\n    q = QueryInfo.from_json(User, query_json)\n    return await c.delete(q)  # response id list: [1]\n\n\nprint(\'Service Running ...\')\nuvicorn.run(app, host=\'0.0.0.0\', port=3000)\n\n```\n\n#### CRUD service with permission\n\nSee [Examples](/examples)\n\n#### Query filter\n\n```python\nfrom pycrud.values import ValuesToUpdate\nfrom pycrud.query import QueryInfo\n\n\nasync def fetch_list():\n    # dsl version\n    q1 = QueryInfo.from_table(User, where=[\n        User.id == 1\n    ])\n\n    # json verison\n    q2 = QueryInfo.from_json(User, {\n        \'id.eq\': 1\n    })\n\n    lst = await c.get_list(q1)\n    print([x.to_dict() for x in lst])\n\n\nasync def update_by_ids():\n    v = ValuesToUpdate({\'nickname\': \'bbb\', \'username\': \'u2\'})\n\n    # from dsl\n    q1 = QueryInfo.from_table(User, where=[\n        User.id.in_([1, 2, 3])\n    ])\n\n    q2 = QueryInfo.from_json(User, {\n        \'id.in\': [1,2,3]\n    })\n\n    lst = await c.update(q1, v)\n    print(lst)\n\n\nasync def complex_filter_dsl():\n    # $or: (id < 3) or (id > 5)\n    (User.id < 3) | (User.id > 5)\n\n    # $and: 3 < id < 5\n    (User.id > 3) & (User.id < 5)\n\n    # $not: not (3 < id < 5)\n    ~((User.id > 3) & (User.id < 5))\n    \n    # logical condition: (id == 3) or (id == 4) or (id == 5)\n    (User.id != 3) | (User.id != 4) | (User.id != 5)\n\n    # logical condition: (3 < id < 5) or (10 < id < 15)\n    ((User.id > 3) & (User.id < 5)) | ((User.id > 10) & (User.id < 15))\n\n\nasync def complex_filter_json():\n    # $or: (id < 3) or (id > 5)\n    QueryInfo.from_json(User, {\n        \'$or\': {\n            \'id.lt\': 3,  \n            \'id.gt\': 5 \n        }\n    })\n    \n    # $and: 3 < id < 5\n    QueryInfo.from_json(User, {\n        \'$and\': {\n            \'id.gt\': 3,  \n            \'id.lt\': 5 \n        }\n    })\n    \n    # $not: not (3 < id < 5)\n    QueryInfo.from_json(User, {\n        \'$not\': {\n            \'id.gt\': 3,  \n            \'id.lt\': 5 \n        }\n    })\n\n    # logical condition: (id == 3) or (id == 4) or (id == 5)\n    QueryInfo.from_json(User, {\n        \'$or\': {\n            \'id.eq\': 3,  \n            \'id.eq.2\': 4,\n            \'id.eq.3\': 5, \n        }\n    })\n\n    # logical condition: (3 < id < 5) or (10 < id < 15)\n    QueryInfo.from_json(User, {\n        \'$or\': {\n            \'$and\': {\n                \'id.gt\': 3,\n                \'id.lt\': 5\n            },\n            \'$and.2\': {\n                \'id.gt\': 10,\n                \'id.lt\': 15\n            }\n        }\n    })\n```\n\n### Operators\n\n| type | operator | text |\n| ---- | -------- | ---- |\n| compare | EQ | (\'eq\', \'==\') |\n| compare | NE | (\'ne\', \'!=\') |\n| compare | LT | (\'lt\', \'<\') |\n| compare | LE | (\'le\', \'<=\') |\n| compare | GE | (\'ge\', \'>=\') |\n| compare | GT | (\'gt\', \'>\') |\n| relation | IN | (\'in\',) |\n| relation | NOT_IN | (\'notin\', \'not in\') |\n| relation | IS | (\'is\',) |\n| relation | IS_NOT | (\'isnot\', \'is not\') |\n| relation | PREFIX | (\'prefix\',) |\n| relation | CONTAINS | (\'contains\',) |\n| logic | AND | (\'and\',) |\n| logic | OR | (\'or\',) |\n',
    'author': 'fy',
    'author_email': 'fy0748@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fy0/pycrud',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.9',
}


setup(**setup_kwargs)
