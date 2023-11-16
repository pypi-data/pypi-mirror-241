# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiogt', 'aiogt.cache', 'aiogt.cache.storage', 'aiogt.transport']

package_data = \
{'': ['*']}

install_requires = \
['urlcon>=1.0.0,<2.0.0']

extras_require = \
{'aiohttp': ['aiohttp>=3.8.6,<4.0.0'],
 'cache': ['redis>=5.0.1,<6.0.0'],
 'httpx': ['httpx>=0.25.1,<0.26.0']}

setup_kwargs = {
    'name': 'aiogt',
    'version': '1.0.0.post1',
    'description': '',
    'long_description': '# Simple async Google Translate library\n\n#### Instalation:\n```pip install aiogt[aiohttp]``` or ```pip install aiogt[httpx]```\n\n#### Featrures\n* Fast and reliable - it uses the same servers that translate.google.com uses\n* Support for httpx and aiohttp\n* Fully asyncio support\n* Simple result caching\n\n#### Example\n```python\nfrom asyncio import run\n\nfrom aiogt import Translaitor\n\n\nasync def main():\n    t = Translaitor()\n    print(await t.translate("Hello", target=\'ru\', source=\'en\'))\n\n    await t.transport.close()\n\nrun(main())\n```',
    'author': 'Robert Stoul',
    'author_email': 'rekiiky@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
