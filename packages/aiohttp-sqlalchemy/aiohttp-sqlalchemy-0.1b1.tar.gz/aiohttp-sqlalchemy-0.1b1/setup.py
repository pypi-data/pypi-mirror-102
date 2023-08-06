# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohttp_sqlalchemy']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy', 'aiohttp']

setup_kwargs = {
    'name': 'aiohttp-sqlalchemy',
    'version': '0.1b1',
    'description': 'SQLAlchemy >= 1.4 support for aiohttp.',
    'long_description': "==================\naiohttp-sqlalchemy\n==================\n\nSQLAlchemy >= 1.4 support for aiohttp.\n\nInstall\n-------\n::\n\n    pip install aiohttp-sqlalchemy\n\n\nExample\n-------\nInstall aiosqlite for work with sqlite3: ::\n\n  pip install aiosqlite\n\nRun this code:\n\n.. code-block:: python\n\n  from aiohttp import web\n  import aiohttp_sqlalchemy\n  from aiohttp_sqlalchemy import sa_engine, sa_middleware\n  from datetime import datetime\n  import sqlalchemy as sa\n  from sqlalchemy import orm\n  from sqlalchemy.ext.asyncio import create_async_engine\n\n\n  metadata = sa.MetaData()\n  Base = orm.declarative_base(metadata=metadata)\n\n\n  class Request(Base):\n      __tablename__ = 'requests'\n      id = sa.Column(sa.Integer, primary_key=True)\n      timestamp = sa.Column(sa.DateTime(), default=datetime.now)\n\n\n  async def main(request):\n      async with request.app['sa_main'].begin() as conn:\n          await conn.run_sync(Base.metadata.create_all)\n\n      async with request['sa_main'].begin():\n          request['sa_main'].add_all([Request()])\n          result = await request['sa_main'].execute(sa.select(Request))\n          data = {r.id: r.timestamp.isoformat() for r in result.scalars()}\n          return web.json_response(data)\n\n\n  app = web.Application(middlewares=[sa_middleware()])\n  engine = create_async_engine('sqlite+aiosqlite:///')\n  aiohttp_sqlalchemy.setup(app, [sa_engine(engine)])\n  app.add_routes([web.get('/', main)])\n  web.run_app(app)\n\nDocumentation\n-------------\nSee: https://aiohttp-sqlalchemy.readthedocs.io/\n",
    'author': 'Ruslan Ilyasovich Gilfanov',
    'author_email': 'ri.gilfanov@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ri-gilfanov/aiohttp-sqlalchemy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
