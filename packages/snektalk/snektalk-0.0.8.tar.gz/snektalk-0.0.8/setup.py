# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snektalk', 'snektalk.feat']

package_data = \
{'': ['*'], 'snektalk': ['assets/*', 'assets/scripts/*', 'assets/style/*']}

install_requires = \
['coleo>=0.2.1,<0.3.0',
 'hrepr>=0.3.11,<0.4.0',
 'jurigged>=0.2.2,<0.3.0',
 'sanic>=20.9.1,<21.0.0']

entry_points = \
{'console_scripts': ['sktk = snektalk.cli:main',
                     'snektalk = snektalk.cli:main']}

setup_kwargs = {
    'name': 'snektalk',
    'version': '0.0.8',
    'description': 'Advanced Python REPL',
    'long_description': '\n# S N E K T A L K\n\nSnektalk is a groundbreaking new kind of REPL.\n\n* Live code editing!\n* Rich and interactive object representations!\n* Built-in debugger!\n* Connect to remote processes!\n* Not another Jupyter clone\n\n# Features\n\nAt a glance Snektalk might appear similar to Jupyter notebooks, but it follows different paradigms. It has no "cells" and is meant to be used like a straightforward REPL or command line. At the same time, it has many features neither standard REPLs nor Jupyter tend to have.\n\n## Edit functions and data\n\nSimply type `/edit func` and you will be greeted with a small inline editor for the source code of `func`. You may change it and hit `Ctrl+Enter` to change it in the current process, or `Ctrl+Shift+Enter` to save it back into the original file it came from. You can come back to it at any time, of course.\n\nVirtually *any* function can be edited, whether it is yours or comes from a third party library or even the standard library.\n\n`/edit` also works on data structures. You will be given an editable sandbox where you can change dictionaries, reorder lists, change the values of the fields of an object, and so on. Objects can even define a custom `__snek_edit__` method to control how they are edited.\n\n## Rich and interactive representations\n\nSnektalk does not print lists, dictionaries or objects as mere text, but as rich HTML objects.\n\n`Ctrl+Click` (or `Cmd+Click` on Mac) the representation of an object to put it in a temporary variable. This makes it very easy to test or play with objects that are deeply nested in another.\n\nRepresentations are highly customizable and recursive representations can be defined and configured in a snap.\n\nThe representation of exceptions is particularly interesting because each frame is associated to a live editor, so you can simply fix the error right there as you see it.\n\n## Visualization\n\nSnektalk supports elaborate visualizations: plots, graphs, and so on. Integrating a new or existing JavaScript library is mostly a matter of linking it from a CDN and writing a small wrapper.\n\n\n## Debugging\n\n`/debug f(x, y)` will enter a function call in debugger mode. Snektalk\'s debugger is quite similar to `pdb` and the usual `pdb` commands (`step`, `next`, `continue`, etc.) should work just the same.\n\n\n## Threads\n\n`/thread f(x, y)` will run `f(x, y)` in a separate thread, which lets you keep working while it\'s running. Each thread is given a mnemonic name so that you can easily `/kill` them.\n',
    'author': 'Olivier Breuleux',
    'author_email': 'breuleux@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/breuleux/snektalk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
