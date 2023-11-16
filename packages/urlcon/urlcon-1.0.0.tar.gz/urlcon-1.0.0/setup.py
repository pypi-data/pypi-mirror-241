# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['urlcon']

package_data = \
{'': ['*']}

install_requires = \
['urllib3>=2.0.7,<3.0.0']

setup_kwargs = {
    'name': 'urlcon',
    'version': '1.0.0',
    'description': '',
    'long_description': '# urlcon\nSimple url constructor library.\n```python\nimport urlcon\n\nc = urlcon.Constructor("api.example.org")\n\nprint(c)\n\nc = c / "api" / ["v2", "get_smth"]\n\nprint(c)\n```\n',
    'author': 'Robert Stoul',
    'author_email': 'rekiiky@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
