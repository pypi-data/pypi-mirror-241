
'''
This modules is designed to be an entry point in pyproject.toml. See the
[project.scripts] section there. It allows to use the tasks defined in
.tasks anywhere.
'''

import platform
import sys

from invoke import Collection, Program

from .. import tasks
from . import __version__


if platform.uname().system != 'Windows':
    # Make sure we run in a pseudo terminal. Otherwise, no color output.
    sys.argv.insert(1, '--pty')

program = Program(namespace=Collection.from_module(tasks),
                  version=f'{__version__}')
