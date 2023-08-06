# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kt_cambio']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0']

entry_points = \
{'console_scripts': ['brlusd = kt_cambio.cli:brlusd',
                     'usdbrl = kt_cambio.cli:usdbrl']}

setup_kwargs = {
    'name': 'kt-cambio',
    'version': '0.2.1',
    'description': 'Conversor de moedas',
    'long_description': '# kt-cambio\nConversor de moedas.  \n  \n## Pré-requisitos\n  Python instalado e disponível no terminal de comandos.  \n    \n## Instalação\n```cmd\npip install kt-cambio\n```\n\n## Uso\n\n```cmd\nbrlusd [--cambio <CAMBIO>] <REAL>\n```\nOnde:  \nREAL Valor em real.  \n--cambio, -c Càmbio do dólar.  \nExemplo:  \n```cmd\nbrlusd 5000.00\n909.09\n```\n  \n```cmd\nusdbrl [--cambio <CAMBIO>] <DOLAR>\n```\nOnde:  \nDOLAR Valor em dólar.  \n--cambio, -c Càmbio do dólar.  \nExemplo:  \n```cmd\nusdbrl 909.09\n4999.99\n```\n',
    'author': 'Valmir Franca',
    'author_email': 'vfranca3@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vfranca/kt-cambio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
