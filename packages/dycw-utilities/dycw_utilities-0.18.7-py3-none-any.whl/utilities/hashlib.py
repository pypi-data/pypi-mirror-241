from __future__ import annotations

from hashlib import md5
from pickle import dumps
from typing import Any


def md5_hash(obj: Any, /) -> str:
    """Compute the MD5 hash of an arbitrary object."""
    if isinstance(obj, bytes):
        return md5(obj, usedforsecurity=False).hexdigest()
    if isinstance(obj, str):
        return md5_hash(obj.encode())
    return md5_hash(dumps(obj))


__all__ = [
    "md5_hash",
]
