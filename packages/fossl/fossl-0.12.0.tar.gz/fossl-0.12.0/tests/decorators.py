
import inspect
import os
import shutil
from functools import wraps
from pathlib import Path


def isolate(test_case):
    '''
    This is a decorator for unit test cases. It creates a temporary
    directory for the unit test function to work in. Its location is
    ./tmp/<testcase_name>/ in the directory containing the test module.
    It the test case succeeds, the tmp dir is removed. If an assertion
    fails, the tmp dir is not removed so its content may be inspected
    for errors.
    '''
    @wraps(test_case)
    def decorator(*args, **kwargs):
        calling_module = inspect.getfile(test_case)
        calling_module_path = Path(calling_module).resolve().parent
        cwd = Path.cwd().resolve()
        home = os.environ['HOME']
        tmpdir = calling_module_path / 'tmp' / test_case.__name__
        if tmpdir.exists():
            shutil.rmtree(tmpdir)
        tmpdir.mkdir(parents=True)
        os.chdir(tmpdir)
        os.environ['HOME'] = str(tmpdir)
        if os.environ.get('USERPROFILE'):
            os.environ['USERPROFILE'] = str(tmpdir)
        cleanup = True
        try:
            test_case(*args, **kwargs)
        except AssertionError:
            cleanup = False
            raise
        except Exception:
            cleanup = False
            raise
        finally:
            os.chdir(cwd)
            os.environ['HOME'] = home
            if os.environ.get('USERPROFILE'):
                os.environ['USERPROFILE'] = home
            if cleanup:
                shutil.rmtree(tmpdir)
    return decorator
