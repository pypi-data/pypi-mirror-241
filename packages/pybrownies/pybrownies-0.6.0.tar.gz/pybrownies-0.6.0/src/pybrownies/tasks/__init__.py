
'''
Tools for building and publishing the project, using the invoke task
manager.

For instance,
% invoke test -c
to run all unit tests and determine coverage.

To list all tasks:
% invoke --list
or short
% invoke -l
Use the built-in help feature to see what a task does e.g.
% invoke test -h
'''

from functools import wraps
from pathlib import Path
import shutil
import sys
import webbrowser

try:
    from tomllib import load as load_toml
except ModuleNotFoundError:
    from tomli import load as load_toml

from invoke import task

BOLD = "\033[1m"
OFF = "\033[0m"


__version__ = '0.3.0'


# Note: ANSI escape codes will be stripped off outputs unless invoke is
# told to use a pseudo-terminal (option --pty). So either 'invoke' or
# 'inv' or both should be aliased as e.g. alias invoke="invoke --pty".
# Our own entry point in __main__ silently injects --pty in to the
# arguments list.
# On Windows? Shrug, didn't try.


def requires(tooling: str):
    '''
    Decorator for tasks which require a specific tool to be installed.
    If a tool is missing the decorator will emit a message and abort the
    task.
    '''
    def decorator(decorated_function):
        @wraps(decorated_function)
        def wrapper(*args, **kwargs):
            if not shutil.which(tooling):
                print(f'This task requires {BOLD}{tooling}{OFF}, which is '
                       'not installed. You can\n'
                      f'{BOLD}pip install {tooling}{OFF}\n'
                       'or\n'
                      f'{BOLD}pip install pybrownies"[full]"{OFF}\n'
                       'and run this task again.')
                return
            decorated_function(*args, **kwargs)
        return wrapper
    return decorator


@task(help={
    'pycaches': 'recursively remove __pycache__/ folders as well',
    'venvs': 'remove anything that starts with .venv* as well'
})
def clean(context, pycaches=False, venvs=False):   # noqa: C901
    '''Remove non-code from the project.

       Deletes files and folders matching .coverage*, .*_cache, .tox.'''
    for path in Path().glob('.coverage*'):
        if path.exists():
            context.run(rf'rm -rf {path}')
    for path in ['.mypy_cache/', '.pytest_cache/', '.tox']:
        if Path(path).exists():
            context.run(rf'rm -rf {path}')
    if pycaches:
        for path in Path().glob('**/__pycache__'):
            context.run(rf'rm -rf {path}')
    if venvs:
        for path in Path().glob('.venv*'):
            context.run(rf'rm -rf {path}')


@task
def covreport(context):
    '''Show the coverage report in the default browser.'''
    #cmd = ''
    index = '.coverage_report/index.html'
    report = Path.cwd().resolve() / index
    if not report.exists():
        print(f'There is no coverage report file here ({index}).',
              file=sys.stderr)
        return
    url = f'file://{str(report)}'
    webbrowser.open(url)


@task
@requires('flit')
def dist(context):
    '''
    Create the sdist and wheel for the distribution of the project.

    This exists more for documentation than anything else.
    Just run flit build instead.
    '''
    context.run('flit build')


@task
@requires('flake8')
@requires('pylint')
def lint(context):
    '''
    Runs pylint and flake8 on every Python package within this project.
    '''
    for initpy in Path().glob('*/__init__.py'):
        print(f'Running {BOLD}pylint{OFF} in {BOLD}{initpy.parent}{OFF}')
        context.run(f'pylint --exit-zero {initpy.parent}')
    print(f'Running {BOLD}flake8{OFF}')
    context.run('flake8')


@task(help={
    'pypi': 'publish on pypi.org instead of test.pypi.org',
    'show': 'show the new page in the web browser',
})
@requires('flit')
def publish(context, pypi=False, show=False):
    '''
    Publishes the project on TestPyPI, or on PyPI with the --pypi option.
    '''
    repo = ' --repository testpypi' if not pypi else ''
    context.run(f'flit publish{repo}')
    if not show:
        return
    pyproj = Path('pyproject.toml')
    if not pyproj.exists():
        return
    with open(pyproj, 'rb') as fp:
        toml = load_toml(fp)
    project = toml['project'].get('name')
    if not project:
        return
    prefix = 'test.' if not pypi else ''
    url = f'https://{prefix}pypi.org/project/{project}/'
    webbrowser.open(url)


@task(help={
    'coverage': 'measure the test coverage as well',
    'options': 'additional options to pass on to pytest'
})
@requires('pytest')
def test(context, coverage=False, options=None):
    '''
    Runs all unit tests, optionally with test coverage.
    '''
    flags = ' --cov --cov-report html' if coverage else ''
    if options:
        flags += f' {options}'
    # if coverage and '--slow' not in flags:
    #     flags += ' --slow'
    context.run(f'pytest -s -v{flags}')
    # Note: Here, the -s option is vital. Without it all tests which check
    # console output for styling will fail.
