# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mplscience', 'mplscience._styledata']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.0,<2.0']}

setup_kwargs = {
    'name': 'mplscience',
    'version': '0.0.1',
    'description': 'Matplotlib style for scientific publications.',
    'long_description': "# mplscience\n\nMatplotlib style for scientific publications. This style keeps things pretty simple and aims to make moderate improvements to the base matplotlib style. It also sets things like the PDF font type to make it easier to interact with figures in Adobe Illustrator.\n\n\n## Usage\n\n```python\nimport mplscience\nmplscience.available_styles()\nmplscience.set_style()\n```\n\nIf you're using Seaborn, you may want to run `sns.reset_orig()` first to clear Seaborn-specific styling.\n\nThe style can also be using in a context like this:\n\n```python\nimport mplscience\nwith mplscience.style_context():\n    plt.plot(x, y)\n```\n\n",
    'author': 'Adam Gayoso',
    'author_email': 'adamgayoso@berkeley.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/adamgayoso/mplscience',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
