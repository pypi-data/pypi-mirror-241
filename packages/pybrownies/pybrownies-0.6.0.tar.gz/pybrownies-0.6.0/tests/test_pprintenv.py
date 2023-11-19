# pylint: disable = missing-function-docstring, missing-module-docstring

import sys

from rich.text import Text

from pybrownies.pprintenv import console, main


def test_pprintenv():
    sys.argv = []
    sys.argv.append('pprintenv')

    with console.capture() as capture:
        main()
    colored = capture.get()
    plain = Text.from_ansi(colored).plain   # console.destyle(colored)
    out = plain[0:200]
    assert 'Environment Variable' in out
    assert 'Value (dir, file, dir or file' in out
