# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['matching_network']

package_data = \
{'': ['*']}

install_requires = \
['quantiphy>=2.13.0,<3.0.0']

setup_kwargs = {
    'name': 'matching-network',
    'version': '0.1.0',
    'description': 'Design lumped-parameters matching networks (L-sections)',
    'long_description': '<div align="right" style="text-align:right"><i><a href="https://urbanij.github.io/">Francesco Urbani</a></i></div>\n\n### Index of Jupyter (IPython) Notebooks\n\n|Title                                                                                                           |\n|----------------------------------------------------------------------------------------------------------------|\n|<a href="https://github.com/urbanij/matching-network/blob/master/aux/L-section_matching_calculations.ipynb">L-section_matching_calculations</a>|\n|<a href="https://github.com/urbanij/matching-network/blob/master/aux/calculations.ipynb">Calculations</a>|\n|<a href="https://github.com/urbanij/matching-network/blob/master/aux/demo_matching_network.ipynb">Demo</a>|\n\n\n\n---\n\n\n[![Downloads](https://pepy.tech/badge/matching-network)](https://pepy.tech/project/matching-network)\n\n\nInstallation\n============\n\n```sh\npip install matching_network\n```\n\n\n\nDocumentation\n=============\n\n\n```python\n>>> import matching_network as mn\n>>>\n>>> impedance_you_have         = 90 + 32j # Ω\n>>> impedance_you_want_to_have = 175      # Ω\n>>>\n>>> frequency                  = 900e6    # Hz\n>>>\n>>> mn.L_section_matching(impedance_you_have, impedance_you_want_to_have, frequency).match()\nFrom (90+32j) Ω to 175 Ω\n\nnormalized starting impedance = (90+32j)Ω/175Ω = 0.51429+0.18286j\n\n#solutions: 2\n\nseries-shunt\n    Series Inductor:\n    X = 55.464 Ω ⇔ B = -18.03 mS\n    L = 9.8082 nH  (@ 900 MHz)\n    Shunt Capacitor:\n    X = -180.07 Ω ⇔ B = 5.5533 mS\n    C = 982.04 fF  (@ 900 MHz)\n\nseries-shunt\n    Series Capacitor:\n    X = -119.46 Ω ⇔ B = 8.3707 mS\n    C = 1.4803 pF  (@ 900 MHz)\n    Shunt Inductor:\n    X = 180.07 Ω ⇔ B = -5.5533 mS\n    L = 31.844 nH  (@ 900 MHz)\n\n>>>\n```\n',
    'author': 'Francesco Urbani',
    'author_email': 'francescourbanidue@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/matching-network/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
