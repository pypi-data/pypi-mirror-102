# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pysparkbundle',
 'pysparkbundle.csv',
 'pysparkbundle.csv.lineage',
 'pysparkbundle.delta',
 'pysparkbundle.jdbc',
 'pysparkbundle.json',
 'pysparkbundle.json.lineage',
 'pysparkbundle.lineage',
 'pysparkbundle.lineage.argument',
 'pysparkbundle.parquet',
 'pysparkbundle.read',
 'pysparkbundle.test',
 'pysparkbundle.write']

package_data = \
{'': ['*'], 'pysparkbundle': ['_config/*']}

install_requires = \
['daipe-core>=0.8.0a4,<0.9.0',
 'injecta>=0.10.0,<0.11.0',
 'pyfony-bundles>=0.4.0,<0.5.0']

entry_points = \
{'pyfony.bundle': ['create = pysparkbundle.PySparkBundle:PySparkBundle']}

setup_kwargs = {
    'name': 'pyspark-bundle',
    'version': '0.1.0a1',
    'description': 'PySpark bundle for the Daipe Framework',
    'long_description': '# Datalake bundle\n\nThis bundle allows you to easily create and manage pyspark(house) based on the [Daipe Framework](https://www.daipe.ai).  \n\n## Resources\n\n* [Documentation](https://docs.daipe.ai/data-pipelines-workflow/managing-pyspark/)\n',
    'author': 'Jiri Koutny',
    'author_email': 'jiri.koutny@datasentics.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/daipe-ai/pyspark-bundle',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
