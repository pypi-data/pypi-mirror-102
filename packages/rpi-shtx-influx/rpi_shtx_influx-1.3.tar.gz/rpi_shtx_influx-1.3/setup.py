# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rpi_shtx_influx']

package_data = \
{'': ['*']}

install_requires = \
['adafruit-circuitpython-si7021>=3.3.3,<4.0.0',
 'influxdb-client>=1.16.0,<2.0.0']

entry_points = \
{'console_scripts': ['rpi_shtx_influx = rpi_shtx_influx.tool:main']}

setup_kwargs = {
    'name': 'rpi-shtx-influx',
    'version': '1.3',
    'description': 'Check temperature using Raspberry Pi and SHT4 sensor, logging to InfluxDB 2.0',
    'long_description': '# rpi-temperature\nCheck temperature using Raspberry Pi and SHT4 sensor\n',
    'author': 'Nathaniel Waisbrot',
    'author_email': 'code@waisbrot.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
