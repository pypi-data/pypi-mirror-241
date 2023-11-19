# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['concourseatom']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'pydantic-yaml>=0.8.0,<0.9.0',
 'ruamel.yaml>=0.17.21,<0.18.0']

entry_points = \
{'console_scripts': ['concmerge = concourseatom.tools:cli']}

setup_kwargs = {
    'name': 'concourseatom',
    'version': '0.3.0',
    'description': 'Read Concourse Pipelines and intelligently allowing pipelines to be built from snipits',
    'long_description': '# concourseatom\n\nThis project provides a merge funtion to intelligently merge concourse jobs together.\n\n\n# Rewrites in merge\n\nWhen a pipeline is merging with another then it scans the names of the resources to identify it there are any duplicate resource types and if so then it plans rewrites of the Right Hand Side pipeine (on the merge funtion call). The process also scans for re-use of the same name for different resource types and plans similar rewrites for those as well.\n\nThis process is then similarily applied to resources.\n\nFinally the rewrites are then applied to the jobs recursively to modify the resource types of the get and put names to match the resources.\nIt is also necessary to consider the name collisions of names of the handles of the resource not just there contents. These are identied as the objects that are the result of get and put and task mapped objects.\n\n\n# Issues\n\nCapture issues here to look at:\n\n* [ ] In_parallel objects inside In_parallel objects. Seems to be triggering issues with sort order (may not be consistent) so results in comparisons of types that are not same.\n',
    'author': 'Ben Greene',
    'author_email': 'BenJGreene@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/PolecatWorks/concourseatom',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
