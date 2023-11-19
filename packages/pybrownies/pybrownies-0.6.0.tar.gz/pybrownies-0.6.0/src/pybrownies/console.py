
'''
This module has two purposes, only:
1) Provide a console instance for the whole package.
2) Initialize the style for the command line help.
'''

from rich.console import Console
from rich_argparse_plus import RichHelpFormatterPlus


console = Console()

RichHelpFormatterPlus.choose_theme('black_and_white')
RichHelpFormatterPlus.styles['argparse.args'] = 'default'
RichHelpFormatterPlus.styles['argparse.groups'] = 'bold'
RichHelpFormatterPlus.styles['argparse.help'] = 'default'
RichHelpFormatterPlus.styles['argparse.metavar'] = 'default'
RichHelpFormatterPlus.styles['argparse.syntax'] = 'bold'
RichHelpFormatterPlus.styles['argparse.text'] = 'default'
RichHelpFormatterPlus.group_name_formatter = str.title
