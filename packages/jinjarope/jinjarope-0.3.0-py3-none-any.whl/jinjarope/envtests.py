from __future__ import annotations

from collections.abc import Sequence
import datetime
import math

from typing import Any


def is_number(value: Any) -> bool:
    """Try to convert value to a float."""
    try:
        fvalue = float(value)
    except (ValueError, TypeError):
        return False
    return math.isfinite(fvalue)


def _is_list(value: Any) -> bool:
    """Return whether a value is a list."""
    return isinstance(value, list)


def _is_set(value: Any) -> bool:
    """Return whether a value is a set."""
    return isinstance(value, set)


def _is_tuple(value: Any) -> bool:
    """Return whether a value is a tuple."""
    return isinstance(value, tuple)


def _is_dict(value: Any) -> bool:
    """Return whether a value is a tuple."""
    return isinstance(value, dict)


def _to_set(value: Any) -> set[Any]:
    """Convert value to set."""
    return set(value)


def _to_tuple(value: Sequence):
    """Convert value to tuple."""
    return tuple(value)


def _is_datetime(value: Any) -> bool:
    """Return whether a value is a datetime."""
    return isinstance(value, datetime.datetime)


def _is_string_like(value: Any) -> bool:
    """Return whether a value is a string or string like object."""
    return isinstance(value, str | bytes | bytearray)


def is_http_url(string: str) -> bool:
    """Return true when given string represents a HTTP url.

    Arguments:
        string: The string to check
    """
    return string.startswith(("http://", "https://", "www.")) and "\n" not in string


def is_protocol_url(string: str) -> bool:
    """Return true when given string represents any type of URL.

    Arguments:
        string: The string to check
    """
    return "://" in string and "\n" not in string
