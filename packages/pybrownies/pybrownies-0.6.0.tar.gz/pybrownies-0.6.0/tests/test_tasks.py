# pylint: disable = missing-function-docstring

'''
Unit tests for buildtasks/tasks.py
'''

import os
from pathlib import Path

from invoke import MockContext, Result

from pybrownies import tasks
from pybrownies.testing import tmpdir


@tmpdir
def test_clean():
    covfile = Path('.coverage')
    covfile.touch()
    dirlist = ['.coverage_report', '.mypy_cache', '.pytest_cache',
               '.tox', '.venv3.11', '__pycache__']
    for path in dirlist:
        Path(path).mkdir()
    os.system('brownie clean --pycaches --venvs')
    assert not covfile.exists()
    for path in dirlist:
        assert not Path(path).exists()


@tmpdir
def test_covreport(capsys):
    open_func = tasks.webbrowser.open
    try:
        ctxt = MockContext(run=Result())
        tasks.webbrowser.open = _webbrowser_open_mock
        tasks.covreport(ctxt)
        _, err = capsys.readouterr()
        assert 'no coverage report file here' in err
        Path('.coverage_report').mkdir()
        Path('.coverage_report/index.html').touch()
        tasks.covreport(ctxt)
        report = Path(covreport)   # covreport is a global variable
        assert report.name == 'index.html'
        assert report.parent.name == '.coverage_report'
    finally:
        tasks.webbrowser.open = open_func
    # ctxt = MockContext(run=Result())
    # result = tasks.covreport(ctxt)
    # assert result is None
    # _, err = capsys.readouterr()
    # assert 'There is no coverage report file here' in err
    # covreport = Path('.coverage_report')
    # covreport.mkdir()
    # (covreport/'index.html').touch()
    # ctxt = MockContext(run=Result('open -a Safari'))
    # result = tasks.covreport(ctxt)
    # assert result is None

# def _get_covreport() -> str:
#     return covreport

def _webbrowser_open_mock(url):
    global covreport
    covreport = url


@tmpdir
def test_dist():
    ctxt = MockContext(run=Result('pyproject.toml does not exist'))
    result = tasks.dist(ctxt)
    # print(f'{result.stderr=}')
    # print(f'{result.stdout=}')
    # print(f'{result.pty=}')
    # print(f'{result.exited=}')
    # print(f'{result.failed=}')
    # print(f'{result.ok=}')
    # print(f'{result.return_code=}')
    assert result is None
    # assert 'pyproject.toml does not exist' in result.stdout
    # assert 0 == result.return_code


def test_requires(capsys):
    @tasks.requires('foo bar')
    def fake_func(*args, **kwargs):
        pass
    fake_func()
    out, _ = capsys.readouterr()
    assert 'not installed' in out
    assert 'pip install' in out
