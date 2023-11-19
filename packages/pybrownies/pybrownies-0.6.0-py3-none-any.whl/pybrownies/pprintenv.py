#!/usr/bin/env python3

'''
Displays the currently active shell environment as a table, sorted
alphabetically. Color-coding is used to highlight directory and
file names. Environment variables such as PATH which contain colon-
separated lists are printed line by line to improve readability.
'''

import argparse
from os import environ as env, path as ospath
from pathlib import Path

from rich.table import Table

from .console import console, RichHelpFormatterPlus


def main():
    '''Pretty-prints the current shell environment.'''
    parser = argparse.ArgumentParser(
        description='Pretty-prints the current shell environment.',
        formatter_class=RichHelpFormatterPlus,
    )
    parser.parse_args()

    table = Table(show_edge=True)
    table.add_column('Environment Variable', justify='left', no_wrap=True)
    table.add_column('Value ('
                     '[dodger_blue1]dir[/], [green3]file[/], '
                     '[orange3]dir or file does not exist[/])',
                     justify='left')
    for name in sorted(env):
        value = env[name]
        if ospath.sep in value:
            new_value = ''
            for path_part in value.split(ospath.pathsep):
                path_part = path_part.strip()
                if not path_part:
                    continue
                path = Path(path_part)
                color = 'dodger_blue1' if path.is_dir() else 'orange3'
                color = 'green3' if path.is_file() else color
                new_value += f'[{color}]{path_part}[/]{ospath.pathsep}\n'
            if value.endswith(ospath.pathsep):
                # Preserve the (semi-)colon because the environment variable
                # ends with it, too.
                value = new_value.rstrip('\n')
            else:
                # Strip off (semi-)colons because they were added when
                # building new_value.
                value = new_value.rstrip(f'{ospath.pathsep}\n')
        table.add_row(name, value)
    console.print(table)


if __name__ == '__main__':
    main()
