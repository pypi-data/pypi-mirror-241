#!/usr/bin/env python3
# pylint: disable=line-too-long
'''
whichpy locates Python modules and packages.
'''

import argparse
from importlib import import_module
from pathlib import Path
import sys

from .console import console, RichHelpFormatterPlus


def find_in_syspath(name):
    '''
    Attempts to locate the module or package by scanning the directories
    in Python's sys.path. This will locate modules/packages which are
    installed outside a currently active virtual environment.
    '''
    modpkg = None
    name = name.replace('.', '/')
    for path in sys.path:
        mod = Path(f'{path}/{name}.py')
        pkg = Path(f'{path}/{name}/__init__.py')
        if mod.exists():
            modpkg = mod
            break
        if pkg.exists():
            modpkg = pkg
            break
    return str(modpkg) if modpkg else None


def find_by_import(name):
    '''
    Tries to import the module/package. If a virtual environment is
    active, this will fail to find modules/packages which are not
    installed in the venv.
    '''
    try:
        modpkg = import_module(name)
    except ModuleNotFoundError:
        modpkg = None
    return modpkg.__file__ if modpkg else None


def main():
    # pylint: disable=missing-function-docstring
    parser = argparse.ArgumentParser(
        description='Locate where a Python module or package is '
                    'installed and display information on the '
                    'module/package.',
                    formatter_class=RichHelpFormatterPlus,
    )
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='verbose output')
    parser.add_argument('name',
                        type=str,
                        help='name of the module or package')
    args = parser.parse_args()
    modpkg = find_by_import(args.name) or find_in_syspath(args.name)
    if not modpkg:
        if args.verbose:
            console.print('Not found.')
        return False

    if args.verbose:
        filepath = Path(modpkg)
        installed = filepath.parent
        name = filepath.name
        kind = 'module'
        if filepath.name == '__init__.py':
            installed = filepath.parent.parent
            name = str(filepath.parent.name)
            kind = 'package'
        console.print(f'[b]{name}[/] is a {kind}. It is installed in')
        console.print(f'{installed}')
    else:
        console.print(modpkg)

    return True


if __name__ == '__main__':
    main()
