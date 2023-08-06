# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['typed_args']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'typed-args',
    'version': '0.5.0a1',
    'description': '',
    'long_description': None,
    'author': 'SunDoge',
    'author_email': '384813529@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
