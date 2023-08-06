# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cgt_calc', 'cgt_calc.parsers', 'cgt_calc.resources']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=2.11.3,<3.0.0']

entry_points = \
{'console_scripts': ['cgt-calc = cgt_calc.main:main']}

setup_kwargs = {
    'name': 'cgt-calc',
    'version': '0.1.1',
    'description': 'UK capital gains tax calculator for Schwab and Trading212 accounts',
    'long_description': '# UK capital gains calculator\n\n[![CI](https://github.com/KapJI/capital_gains_calculator/actions/workflows/ci.yml/badge.svg)](https://github.com/KapJI/capital_gains_calculator/actions)\n[![PyPI version](https://img.shields.io/pypi/v/cgt-calc)](https://pypi.org/project/cgt-calc/)\n\nCalculate capital gains tax by transaction history exported from Schwab/Trading212 and generate PDF report with calculations.\n\nAutomatically convert all prices to GBP and apply HMRC rules to calculate capital gains tax: "same day" rule, "bed and breakfast" rule, section 104 holding.\n\n## Report example\n\n[calculations_example.pdf](https://github.com/KapJI/capital_gains_calculator/blob/main/calculations_example.pdf)\n\n## Installation\n\nInstall it with [pipx](https://pipxproject.github.io/pipx/) (or regular pip):\n\n```shell\npipx install cgt-calc\n```\n\n**`pdflatex` is required to generate the report.**\n\n### MacOS\n\n```shell\nbrew install --cask mactex-no-gui\n```\n\n### Debian based\n\n```shell\napt install texlive-latex-base\n```\n\n### Windows\n\n[Install MiKTeX.](https://miktex.org/download)\n\n## Usage\n\n-   `schwab_transactions.csv`: the exported transaction history from Schwab since the beginning. Or at least since you first acquired the shares, which you were holding during the tax year. You can probably convert transactions from other brokers to Schwab format.\n-   `trading212/`: the exported transaction history from Trading212 since the beginning. Or at least since you first acquired the shares, which you were holding during the tax year. You can put several files here since Trading212 limit the statements to 1 year periods.\n-   `GBP_USD_monthly_history.csv`: monthly GBP/USD prices from [gov.uk](https://www.gov.uk/government/collections/exchange-rates-for-customs-and-vat).\n-   `initial_prices.csv`: stock prices in USD at the moment of vesting, split, etc.\n-   Run `cgt-calc --tax_year 2020 --schwab schwab_transactions.csv --trading212 trading212/` (you can omit the brokers you don\'t use)\n-   Use `cgt-calc --help` for more details/options.\n\n## Disclaimer\n\nPlease be aware that I\'m not a tax adviser so use this data at your own risk.\n\n## Contribute\n\nAll contributions are highly welcomed.\nIf you notice any bugs please open an issue or send a PR to fix it.\n\nFeel free to add parsers to support transaction history from more brokers.\n\n## Testing\n\nThis project uses [Poetry](https://python-poetry.org/) for managing dependencies.\n\n-   To test it locally you need to [install it](https://python-poetry.org/docs/#installation).\n-   After that run `poetry install` to install all dependencies.\n-   Then activate `pre-commit` hook: `poetry run pre-commit install`\n\nYou can also run all linters and tests manually with this command:\n\n```shell\npoetry run pre-commit run --all-files\n```\n',
    'author': 'Ruslan Sayfutdinov',
    'author_email': 'ruslan@sayfutdinov.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/KapJI/capital_gains_calculator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
