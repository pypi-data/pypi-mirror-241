# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytorch_tabr']

package_data = \
{'': ['*']}

install_requires = \
['black>=23.9.1,<24.0.0',
 'catboost>=1.2.2,<2.0.0',
 'delu>=0.0.22,<0.0.23',
 'einops>=0.7.0,<0.8.0',
 'faiss-gpu>=1.7.2,<2.0.0',
 'flake8>=6.1.0,<7.0.0',
 'ipython>=8.17.2,<9.0.0',
 'ipywidgets>=8.1.1,<9.0.0',
 'notebook>=7.0.4,<8.0.0',
 'numpy==1.26.0',
 'pandas>=2.1.1,<3.0.0',
 'plotly>=5.17.0,<6.0.0',
 'scikit-learn>=1.3.1,<2.0.0',
 'torch>=2.0.0,!=2.0.1',
 'torchvision>=0.15.1,<0.16.0,!=0.15.2',
 'tqdm>=4.66.1,<5.0.0',
 'ucimlrepo>=0.0.3,<0.0.4',
 'xgboost>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'pytorch-tabr',
    'version': '0.1.0',
    'description': '',
    'long_description': '# pytorch-tabr\n\n## Overview\n\npytorch-tabr is a Python package that provides a PyTorch wrapper implementation of TabR, a deep learning model for tabular data. The original implementation can be found here:\n[TabR: Unlocking the Power of Retrieval-Augmented Tabular Deep Learning](https://github.com/yandex-research/tabular-dl-tabr) This package allows for easy and efficient modeling of both classification and regression tasks using tabular data. It includes support for various kinds of embeddings and customizations to cater to different types of tabular datasets.\n\n## Features\n\n- **TabR Model**: Core deep learning model for tabular data.\n- **Classification and Regression**: Support for both classification (`TabRClassifier`) and regression (`TabRRegressor`) tasks.\n- **Custom Embeddings**: Supports categorical, numerical, and other types of embeddings.\n- **Efficient Handling of Data**: Efficient data loaders and utilities for handling tabular data.\n\n## Installation\n\n```bash\npip install pytorch-tabr\n```\n\n## Usage\n\n### Basic example\n\n```python\nfrom pytorch_tabr import TabRClassifier, TabRRegressor\n\n# For a classification task\nclassifier = TabRClassifier(cat_indices=[0, 2], cat_cardinalities=[3, 5])\n# Training and prediction...\n\n# For a regression task\nregressor = TabRRegressor(cat_indices=[1, 3], cat_cardinalities=[4, 2])\n# Training and prediction...\n```\n\n## API Overview\n- **TabRClassifier**: Model for classification tasks.\n- **TabRRegressor**: Model for regression tasks.\n- **TabR**: Base module implementing the TabR architecture.\n',
    'author': 'Eduardo Carvalho Pinto',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.13',
}


setup(**setup_kwargs)
