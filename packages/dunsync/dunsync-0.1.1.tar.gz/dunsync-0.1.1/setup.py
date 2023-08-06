# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dunsync']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dunsync',
    'version': '0.1.1',
    'description': 'Identical to unsync, but supports cpu-bound continuation functions',
    'long_description': "# dunsync\n\nIdentical to [unsync](https://github.com/alex-sherman/unsync), except that continuation callbacks receives the result of the Unfuture\nrather than the Unfuture itself. This allows cpu-bound `@unsync` functions to be chained together with other regular functions and IO-bound `@unsync` functions, as long as the result is pickleble. \n\n## Example\n\n```python\nfrom dunsync import unsync\nimport asyncio\nimport time\n\n@unsync()  # Will run in an asyncio event loop\nasync def download_data(url):\n    await asyncio.sleep(1)\n    return 'data'\n\n@unsync(cpu_bound=True)  # Will run in a separate process\ndef process_data(data):\n    time.sleep(1)\n    return 'processed data'\n\n@unsync()  # Will run in a separate thread\ndef store_processed_data(data):\n    time.sleep(1)\n    return 'Done'\n\ntasks = [\n    download_data(url).then(process_data).then(store_processed_data)\n    for url in ['url1', 'url2', 'url3']\n]\n\nfor task in tasks:\n    print(task.result())\n```\n\nReplacing dunsync with unsync in the above example results in the error `TypeError: cannot pickle '_asyncio.Task' object`,\nsince the Unfuture wraps other objects (either `asyncio.Task`, as in this example, or `threading.Thread`) which cannot be pickled\nin order to be passed to a separate process.\n\n## Installation\n\nUsing pip:\n```shell\npip install dunsync\n```\n\nUsing pipenv:\n```shell\npipenv install dunsync\n```\n\nUsing poetry:\n```shell\npoetry add dunsync\n```\n",
    'author': 'Daniel Hjertholm',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/danhje/dunsync',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
