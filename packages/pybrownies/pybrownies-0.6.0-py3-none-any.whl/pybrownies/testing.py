
'''
A decorator for test cases that need to work with temporary files and
directories.
'''

from functools import wraps
from os import chdir
from pathlib import Path
from shutil import rmtree
import inspect


def tmpdir(decorated_function):
    '''
    This is a decorator for unit test cases. It creates a temporary
    directory for the unit test function to work in. Its location is
    ./tmp/<testcase_name>/ in the directory containing the test module.
    It the test case succeeds, the tmp dir is removed. If an assertion
    fails, the tmp dir is not removed so its content may be inspected
    for errors.
    '''
    @wraps(decorated_function)
    def decorator(*args, **kwargs):
        calling_module = inspect.getfile(decorated_function)
        calling_module_path = Path(calling_module).resolve().parent
        cwd = Path.cwd().resolve()
        tmpdir = calling_module_path / 'tmp' / decorated_function.__name__
        if tmpdir.exists():
            rmtree(tmpdir)
        tmpdir.mkdir(parents=True)
        chdir(tmpdir)
        cleanup = True
        try:
            decorated_function(*args, **kwargs)
        except AssertionError:
            cleanup = False
            raise
        except Exception:
            cleanup = False
            raise
        finally:
            chdir(cwd)
            if cleanup:
                rmtree(tmpdir)
    return decorator

# I am aware of fixtures, including tmp_path. The problems arises when
# a test case cd's into tmp_path to do its thing, and then an assertion
# fails or an exception occurs: the CWD of the test run is not restored.
