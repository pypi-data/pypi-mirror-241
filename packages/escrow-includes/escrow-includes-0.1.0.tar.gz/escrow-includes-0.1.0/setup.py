# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['escrow_includes',
 'escrow_includes.errors',
 'escrow_includes.helpers',
 'escrow_includes.helpers.drf_helpers']

package_data = \
{'': ['*'], 'escrow_includes': ['app_services/*']}

install_requires = \
['Django>=4.2.7,<5.0.0', 'djangorestframework>=3.14.0,<4.0.0', 'pydantic==1.10']

setup_kwargs = {
    'name': 'escrow-includes',
    'version': '0.1.0',
    'description': 'general lib utils for escrow backend service',
    'long_description': None,
    'author': 'o4codes',
    'author_email': 'oforkansi.shadrach@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
