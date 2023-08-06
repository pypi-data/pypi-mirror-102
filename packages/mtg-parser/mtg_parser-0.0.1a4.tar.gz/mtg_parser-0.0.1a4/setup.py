# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mtg_parser']

package_data = \
{'': ['*']}

install_requires = \
['pyparsing>=2.4.7,<3.0.0', 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'mtg-parser',
    'version': '0.0.1a4',
    'description': 'Magic: the Gathering decklist parser',
    'long_description': '# mtg-parser\n\n## How to install\n\n\tpip install mtg-parser\n\n## Run tests\n\nThis project uses `poetry`, please refer to [their website](https://python-poetry.org) on how to install it.\n\nThen, clone the repository and:\n\n\t$ make install lint test\n\n## How to publish a new version\n\n### Test version\n\n\t$ poetry version (premajor|preminor|prepatch|prerelease)\n\t$ make test lint build clean test-publish\n\n### Release version\n\n\t$ poetry version (major|minor|patch)\n\t$ make test lint build clean publish\n\n## How to use\n\n\timport mtg_parser\n\t\n\tdecklist = """\n\t\t1 Atraxa, Praetors\' Voice\n\t\t1 Imperial Seal\n\t\t1 Lim-Dûl\'s Vault\n\t\t1 Jeweled Lotus (CMR) 319\n\t\t1 Llanowar Elves (M12) 182\n\t\t3 Brainstorm #Card Advantage #Draw\n\t"""\n\t\n\tcards = mtg_parser.parse_decklist(decklist)\n\t\n\tfor card in cards:\n\t\tprint(card[\'quantity\'], card[\'card_name\'])\n',
    'author': 'Ludovic Heyberger',
    'author_email': '940408+lheyberger@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lheyberger/mtg-parser',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
