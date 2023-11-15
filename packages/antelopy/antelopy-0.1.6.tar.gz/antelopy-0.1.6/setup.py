# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['antelopy',
 'antelopy.cache',
 'antelopy.exceptions',
 'antelopy.serializers',
 'antelopy.types',
 'antelopy.utils']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=2.4.2,<3.0.0', 'requests>=2.31.0,<3.0.0']

setup_kwargs = {
    'name': 'antelopy',
    'version': '0.1.6',
    'description': 'Python helper for Antelope transaction serialization',
    'long_description': '# antelopy\n\n![Workflow Badge](https://github.com/stuckatsixpm/antelopy/actions/workflows/main.yml/badge.svg?branch=main) ![Python version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue) ![PyPI](https://img.shields.io/pypi/v/antelopy?label=PyPI)\n\n*v0.1.6 - initial release*\n\nDrop-in Python ABI cache for Antelope chains with local serialization support. \n\n## Features\n* Serialization of Antelope built-in types\n* Caches ABIs for faster serialization of actions\n* Support for ABI custom types/variants\n\n## Basic Usage:\n*Note: Reading ABIs uses `requests` and is not asynchronous.*\n\n### Instaliation\n\n```bash\npip install antelopy\n```\n\n### Example with aioeos\n**Loading a contract\'s ABI into the cache:**\n```py\nfrom antelopy import AbiCache\n\nCHAIN_ENDPOINT = "https://wax.eosphere.io"\n\n# Create ABI Cache and read the Atomic Assets contract ABI\nabicache = AbiCache(chain_endpoint=CHAIN_ENDPOINT)\nabicache.read_abi("atomicassets")\n```\n\n\n**Serializing, signing, and pushing a transaction** *(modified version of aioeos\' built-in `EosTransaction.sign_and_push_transaction` function)*\n```py\nimport asyncio\nfrom antelopy import AbiCache\nfrom aioeos import EosAccount, EosJsonRpc, EosTransaction, serializer\n\nCHAIN_ENDPOINT = "https://wax.eosphere.io"\n\n# Create ABI Cache and read the Atomic Assets contract ABI\nabicache = AbiCache(chain_endpoint=CHAIN_ENDPOINT)\nabicache.read_abi("atomicassets")\n\n# Fake Account\nwax_account = EosAccount(\n    name="testaccount1",\n    private_key="your private key"\n)\n\n# \nrpc = EosJsonRpc(CHAIN_ENDPOINT)\n\ntransaction = EosTransaction(\n    # transaction data\n)\nasync def serialize_sign_and_push(transaction: EosTransaction):\n    for action in transaction.actions: \n        if isinstance(action.data, dict):\n            # This {"binargs": serialized_data} structure emulates\n            # the response from the old `abi_json_to_bin` endpoint.\n            abi_bin = {"binargs":abicache.serialize_data(action.account,action.name, action.data)}\n            action.data = abi_cache.unhexlify(abi_bin[\'binargs\'])\n\n    chain_id = await RPC.get_chain_id()\n    serialized_transaction = serializer.serialize(transaction)\n\n    digest = abi_cache.sha256digest(\n        b\'\'.join((chain_id, serialized_transaction, bytes(32)))\n    )\n\n    return await RPC.push_transaction(\n        signatures=[key.sign(digest) for key in [wax_account.key]],\n        serialized_transaction=(\n            abi_cache.hexlify(serialized_transaction).decode()\n        )\n    )\n\nawait serialize_sign_and_push(transaction)\n```\n\n## Todo:\n* Implement remaining types\n* refactor serializers to class based approach, similar to [aioeos](https://github.com/ulamlabs/aioeos/blob/master/aioeos/serializer.py)\n* Implement better type hinting for serialization\n* Expand test coverage\n* Add examples for aioeos, eospy, and pyantelope',
    'author': 'Jake Hattwell',
    'author_email': 'stuck@sixpm.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/stuckatsixpm/antelopy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
