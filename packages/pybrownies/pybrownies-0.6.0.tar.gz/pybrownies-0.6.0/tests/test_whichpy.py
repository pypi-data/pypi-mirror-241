
from pathlib import Path
import sys

from pybrownies.whichpy import console, find_in_syspath, find_by_import, main


def test_find_in_syspath():
    _run_test_with(find_in_syspath)


def test_find_by_import():
    _run_test_with(find_by_import)


def test_main():
    # Look for a package which does not exist.
    sys.argv = ['whichpy', 'richer']
    result = main()
    assert result is False
    with console.capture() as capture:
        sys.argv = ['whichpy', '-v', 'richer']
        result = main()
    assert result is False
    assert 'Not found.' in capture.get()
    # Look for a package that exists in our venv.
    with console.capture() as capture:
        sys.argv = ['whichpy', 'rich']
        result = main()
    assert result is True
    with console.capture() as capture:
        sys.argv = ['whichpy', '--verbose', 'rich']
        result = main()
    assert result is True
    output = capture.get()
    assert 'is a package' in output


def _run_test_with(test_func):
    # Look for a package which does not exist.
    found = test_func('richer')
    assert not found
    # Look for a package that exists in our venv.
    found = test_func('rich')
    assert found is not None
    path = Path(found)
    assert path.name == '__init__.py'
    assert path.parent.name == 'rich'
    # Look for a module that exists in our venv.
    found = test_func('rich.markdown')
    assert found is not None
    path = Path(found)
    assert path.name == 'markdown.py'
    assert path.parent.name == 'rich'
    # Look for a module that does not exist in our venv, but outside.
    found = test_func('traceback')
    assert found is not None
    assert found.endswith('traceback.py')
