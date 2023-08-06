# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['serviceit']

package_data = \
{'': ['*']}

install_requires = \
['tomlkit>=0.7,<1.0', 'typer>=0.3,<1.0']

setup_kwargs = {
    'name': 'serviceit',
    'version': '0.2.0',
    'description': 'Turn any Python function into a service that receives JSON payloads on some port.',
    'long_description': '# Service-it\n\n[![Version status](https://img.shields.io/pypi/status/serviceit?label=status)](https://pypi.org/project/serviceit)\n[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)\n[![Python version compatibility](https://img.shields.io/pypi/pyversions/serviceit?label=Python)](https://pypi.org/project/serviceit)\n[![Version on GitHub](https://img.shields.io/github/v/release/dmyersturnbull/service-it?include_prereleases&label=GitHub)](https://github.com/dmyersturnbull/service-it/releases)\n[![Version on PyPi](https://img.shields.io/pypi/v/serviceit?label=PyPi)](https://pypi.org/project/serviceit)  \n[![Build (Actions)](https://img.shields.io/github/workflow/status/dmyersturnbull/service-it/Build%20&%20test?label=Tests)](https://github.com/dmyersturnbull/service-it/actions)\n[![Coverage (coveralls)](https://coveralls.io/repos/github/dmyersturnbull/service-it/badge.svg?branch=main&service=github)](https://coveralls.io/github/dmyersturnbull/service-it?branch=main)\n[![Maintainability (Code Climate)](https://api.codeclimate.com/v1/badges/6b804351b6ba5e7694af/maintainability)](https://codeclimate.com/github/dmyersturnbull/service-it/maintainability)\n[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dmyersturnbull/service-it/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/service-it/?branch=main)\n[![Created with Tyrannosaurus](https://img.shields.io/badge/Created_with-Tyrannosaurus-0000ff.svg)](https://github.com/dmyersturnbull/mandos)\n\n\nTurn any Python function into a service that receives JSON payloads on some port.\n\nHere’s a trivial example:\n\n```python\nimport serviceit\ndef receiver(payload):\n    print(payload)\nserver = serviceit.server(1533, receiver)\n# Now it will receive JSON on 1533. For convenience:\nserver.client().send(dict(message="hi"))\nprint(server.bytes_processed)\n```\n\n#### More complex example: isolate code\nYou can use this to isolate a component of you code.\nFor example, rdkit can be installed through Conda but not Pip (or Poetry).\nSo, create a service and import it in an Anaconda environment to create a server,\nand in your pip-installed client code.\n\n**In a Conda environment**, create a service that listens on port 1533:\n\n```python\nimport serviceit\n\ndef _receiver(payload):\n    # noinspection PyUnresolvedReferences\n    from rdkit.Chem.inchi import InchiToInchiKey\n    inchikey = InchiToInchiKey(payload["inchi"])\n    print(inchikey)\n\nserver = serviceit.server(1533, _receiver)\n```\n\n**On your pip-install client side:**\n\n```python\nimport serviceit\nclient = serviceit.client(1533)\nclient.send(dict(inchi="InChI=1S/H2O/h1H2"))\n```\n\n\n[New issues](https://github.com/dmyersturnbull/service-it/issues) and pull requests are welcome.\nPlease refer to the [contributing guide](https://github.com/dmyersturnbull/service-it/blob/master/CONTRIBUTING.md).  \nGenerated with [Tyrannosaurus](https://github.com/dmyersturnbull/tyrannosaurus).\n',
    'author': 'Douglas Myers-Turnbull',
    'author_email': None,
    'maintainer': 'Douglas Myers-Turnbull',
    'maintainer_email': None,
    'url': 'https://github.com/dmyersturnbull/service-it',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
