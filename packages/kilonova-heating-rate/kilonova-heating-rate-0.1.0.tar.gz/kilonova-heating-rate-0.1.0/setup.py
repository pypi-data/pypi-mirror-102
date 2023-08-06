# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kilonova_heating_rate']

package_data = \
{'': ['*']}

install_requires = \
['astropy', 'numpy', 'scipy']

setup_kwargs = {
    'name': 'kilonova-heating-rate',
    'version': '0.1.0',
    'description': 'Kilonova light curves from Hotokezaka & Nakar 2019',
    'long_description': '# kilonova-heating-rate\n\nThis is a Python package to calculate kilonova light curves using the\nHotokezaka & Nakar (2019) model, which assumes radioactive heating, a power-law\nvelocity profile, and gray opacities that are a piecewise-constant function of\nvelocity.\n\nThis Python package is based on the original source code release from the 2019\npaper (https://github.com/hotokezaka/HeatingRate), but includes the following\nenhancements:\n\n* **Easy to install** with [Pip], the Python package manager.\n* **Physical units** are integrated with [Astropy], the community Python\n  package for astronomy.\n* **Flexible** specification of opacities: either constant, or piecewise\n  constant as a function of ejecta velocity.\n* **Fast** due to the use of [Numpy] to evaluate the right-hand side of the\n  system of ordinary differential equations that is solved to evalute the light\n  curve.\n\n## To cite\n\nIf you use this work to produce a peer-reviewed journal article, please cite\nthe following papers:\n\n* Korobkin, O., Rosswog, S., Arcones, A., & Winteler, C. 2012, "On the\n  astrophysical robustness of the neutron star merger r-process," *Monthly\n  Notices of the Royal Astronomical Society*, 426, 1940.\n  https://doi.org/10.1111/j.1365-2966.2012.21859.x\n* Hotokezaka, K. & Nakar, E. 2020, "Radioactive Heating Rate of *r*-process\n  Elements and Macronova Light Curve," *Astrophysical Journal*, 891, 152.\n  https://doi.org/10.3847/1538-4357/ab6a98\n\n## To install\n\nInstallation is easy with [Pip]:\n\n    $ pip install kilonova-heating-rate\n\n## To use\n\nSee example code in [example.py].\n\n![Example plot](https://github.com/dorado-science/kilonova-heating-rate/raw/main/example.png)\n\n[Pip]: https://pip.pypa.io\n[Astropy]: https://www.astropy.org\n[Numpy]: https://github.com/numpy/numpy\n[example.py]: https://github.com/dorado-science/kilonova-heating-rate/blob/main/example.py\n',
    'author': 'Bas Dorsman',
    'author_email': 'bas.dorsman@student.uva.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
