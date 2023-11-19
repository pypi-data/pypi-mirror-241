#!/usr/bin/env python3

'''
Pretty-print several text file formats with syntax highlighting.
'''

import argparse
import plistlib
import sys
from pathlib import Path

from bs4 import BeautifulSoup as Soup   # type: ignore
from pygments.cmdline import main as pygmentize
from rich.markdown import Markdown

from .console import console, RichHelpFormatterPlus


def _configure_cli():
    parser = argparse.ArgumentParser(
        description='Outputs text files to the console with syntax '
                    'highlighting.',
        epilog='(*) [i]Ignored for JSON, HTML, and Markdown files.[/]'
               '\n\n'
               'PLIST files are shown as a Python dictionary by default. Use '
               'the -f soup option to use BeautifulSoup as the formatter.',
        formatter_class=RichHelpFormatterPlus,
    )

    parser.add_argument('-f', metavar='FORMATTER',
                        dest='formatter',
                        help='specify the Pygments formatter to use (*)')
    parser.add_argument('-l', metavar='LEXER',
                        help='specify the Pygments lexer to use (*)')
    parser.add_argument('path',
                        type=Path,
                        help='path to the file to show')
    return parser


def format_html(args) -> None:
    with open(args.path) as fid:
        soup = Soup(fid.read(), 'html.parser')
        console.print(soup.prettify(formatter="html"))

# def format_json_dict(args) -> None:
#     with open(args.path) as fid:
#         as_dict = json.load(fid)
#         console.print(as_dict)

def format_json_rich(args) -> None:
    with open(args.path) as fid:
        console.print_json(fid.read())

def format_markdown(args) -> None:
    with open(args.path) as fid:
        console.print(Markdown(fid.read()))

def format_other(args) -> None:
    pygmentize(sys.argv)

def format_plist(args) -> None:
    if args.formatter and args.formatter == 'soup':
        with open(args.path, 'rb') as pl:
            soup = Soup(pl.read(), 'lxml-xml')
            console.print(soup.prettify())
    elif not args.formatter or args.formatter == 'dict':
        with open(args.path, 'rb') as pl:
            as_dict = plistlib.load(pl)
            console.print(as_dict)
    # Another option: pygmentize -l xml filename.plist


formatter = {
    'HTM'   : format_html,
    'HTML'  : format_html,
    # 'JSON'          : format_json_dict,
    # 'JSON-pygments' : format_json_pygments,
    'JSON'     : format_json_rich,
    # 'MD-pygments'   : format_markdown_pygments,
    'MD'       : format_markdown,
    'OTHER' : format_other,
    'PLIST' : format_plist
}


def main():
    parser = _configure_cli()
    args = parser.parse_args()
    ext  = args.path.suffix[1:]
    ext  = ext.upper() if ext else 'OTHER'
    #fmt  = args.formatter if args.formatter else None
    #found = [f for f in ('dict', 'pygments', 'rich') if f.startswith(args.formatter)]
    code = ext if ext in formatter else 'OTHER'
    formatter[code](args)
    #console.print(md_content)


if __name__ == "__main__":
    main()
