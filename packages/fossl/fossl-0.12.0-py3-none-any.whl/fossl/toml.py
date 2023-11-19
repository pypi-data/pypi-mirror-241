
'''
This module provides a toml.load() method for all versions of Python.
'''

from pathlib import Path
from typing import Any, Dict

try:
    import tomllib as toml_r
except ModuleNotFoundError:
    import tomli as toml_r
import tomli_w


def load(path: Path) -> Dict:
    content = None
    with open(path, 'rb') as fp:
        content = toml_r.load(fp)
    return content


def loads(data: str) -> Dict:
    return toml_r.loads(data)


def dump(path: Path, obj: Dict[str, Any]):
    with open(path, 'wb') as fp:
        tomli_w.dump(obj, fp)


def dumps(obj: Dict[str, Any]) -> str:
    return tomli_w.dumps(obj)
