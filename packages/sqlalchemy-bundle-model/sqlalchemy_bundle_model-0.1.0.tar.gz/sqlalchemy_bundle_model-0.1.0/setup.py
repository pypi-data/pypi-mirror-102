# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sqlalchemy_bundle_model']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.3.0']

setup_kwargs = {
    'name': 'sqlalchemy-bundle-model',
    'version': '0.1.0',
    'description': 'An extension to SQLAlchemy to treat aggregated columns and clauses as Models',
    'long_description': '# sqlalchemy_bundle_model\nAn extension to SQLAlchemy to treat aggregated columns and clauses as Models\n\n# usage\n\n```\n>>> from sqlalchemy_bundle_model import BundleModel\n>>> class User(DeclarativeBase):\n...     __tablename__ = "users"\n...     id = Column(BigInteger, primary_key=True)\n...     name = Column(Text, nullable=False)\n...     group_id = Column(ForeignKey("groups.id"), nullable=False)\n...\n...     group = relationship("Group")\n...\n>>> class Group(DeclarativeBase):\n...     __tablename__ = "groups"\n...     id = Column(BigInteger, primary_key=True)\n...     name = Column(Text, nullable=False)\n...\n>>> class GroupUser(BundleModel):\n...     id = col(int, User.id)\n...     name = col(str, User.name)\n...     group_name = col(str, Group.name)\n...\n...     @staticmethod\n...     def join(_query: Query):\n...         return _query.join(User.group)\n...\n>>> session = session_cls()\n>>> query = session.query(GroupUser)\n>>> query = GroupUser.join(query)\n>>> result = query.first()\n>>> result.group_name is not None\n\n```',
    'author': 'Yuichiro Smith',
    'author_email': 'contact@yu-smith.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
