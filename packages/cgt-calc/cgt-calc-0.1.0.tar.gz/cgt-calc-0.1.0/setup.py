# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cgt_calc', 'cgt_calc.parsers']

package_data = \
{'': ['*'], 'cgt_calc': ['resources/*']}

install_requires = \
['Jinja2>=2.11.3,<3.0.0']

entry_points = \
{'console_scripts': ['cgt-calc = cgt_calc.main:main']}

setup_kwargs = {
    'name': 'cgt-calc',
    'version': '0.1.0',
    'description': 'UK capital gains tax calculator for Schwab and Trading212 accounts',
    'long_description': '# UK capital gains calculator\n\n[![CI](https://github.com/KapJI/capital_gains_calculator/workflows/CI/badge.svg)](https://github.com/KapJI/capital_gains_calculator/actions)\n\nCalculate capital gains tax by transaction history exported from Schwab/Trading212 and generate PDF report with calculations. Automatically convert all prices to GBP and apply HMRC rules to calculate capital gains tax: "same day" rule, "bed and breakfast" rule, section 104 holding.\n\n## Report example\n\n[calculations_example.pdf](https://github.com/KapJI/capital_gains_calculator/blob/main/calculations_example.pdf)\n\n## Setup\n\nOn Mac:\n\n```shell\nbrew install --cask mactex-no-gui\npip install -r requirements.txt\n```\n\n## Usage\n\n-   `schwab_transactions.csv`: the exported transaction history from Schwab since the beginning. Or at least since you first acquired the shares, which you were holding during the tax year. You can probably convert transactions from other brokers to Schwab format.\n-   `trading212/`: the exported transaction history from Trading212 since the beginning. Or at least since you first acquired the shares, which you were holding during the tax year. You can put several files here since Trading212 limit the statements to 1 year periods.\n-   `GBP_USD_monthly_history.csv`: monthly GBP/USD prices from [gov.uk](https://www.gov.uk/government/collections/exchange-rates-for-customs-and-vat).\n-   `initial_prices.csv`: stock prices in USD at the moment of vesting, split, etc.\n-   Run `python3 calc.py --tax_year 2020 --schwab schwab_transactions.csv --trading212 trading212/` (you can omit the brokers you don\'t use)\n-   Use `python3 calc.py --help` for more details/options.\n\n## Testing\n\n```shell\npip install pytest\npytest\n```\n\n## Disclaimer\n\nPlease be aware that I\'m not a tax adviser so use this data at your own risk.\n\n## Contribute\n\nIf you notice any bugs feel free to open an issue or send a PR.\n',
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
