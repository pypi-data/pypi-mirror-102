# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flowi',
 'flowi.components',
 'flowi.components.data_preparation',
 'flowi.components.load',
 'flowi.components.metrics',
 'flowi.components.model_selection',
 'flowi.components.models',
 'flowi.components.preprocessing',
 'flowi.components.save',
 'flowi.flow_chart',
 'flowi.prediction',
 'flowi.utilities']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=1.6.0,<2.0.0',
 'dask-ml>=1.8.0,<2.0.0',
 'dask>=2021.4.0,<2022.0.0',
 'distributed>=2021.4.0,<2022.0.0',
 'pandas>=1.2.4,<2.0.0',
 'scikit-learn>=0.24.1,<0.25.0']

setup_kwargs = {
    'name': 'flowi',
    'version': '0.2.1',
    'description': '',
    'long_description': None,
    'author': 'Leonardo Silva',
    'author_email': 'psilva.leo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
