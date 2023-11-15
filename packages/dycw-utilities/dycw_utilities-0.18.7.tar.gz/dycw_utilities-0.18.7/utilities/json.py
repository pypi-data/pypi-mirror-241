from __future__ import annotations

import datetime as dt
from json import dumps
from pathlib import Path
from typing import Any


def serialize(
    x: Any,
    /,
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    indent: int | str | None = None,
    separators: tuple[str, str] | None = None,
    sort_keys: bool = False,
    **kwargs: Any,
) -> str:
    """Serialize an object."""
    return dumps(
        x,
        skipkeys=skipkeys,
        ensure_ascii=ensure_ascii,
        check_circular=check_circular,
        allow_nan=allow_nan,
        indent=indent,
        separators=separators,
        default=_default,
        sort_keys=sort_keys,
        **kwargs,
    )


def _default(x: Any, /) -> str:
    """Extension for the JSON serializer."""
    if isinstance(x, dt.date):
        return x.isoformat()
    if isinstance(x, Path):
        return str(x)
    if isinstance(x, set):
        inner = serialize(sorted(x))
        return f"set({inner})"
    if isinstance(x, frozenset):
        inner = serialize(sorted(x))
        return f"frozenset({inner})"
    msg = f"Invalid type: {x}"
    raise TypeError(msg)


__all__ = [
    "serialize",
]
