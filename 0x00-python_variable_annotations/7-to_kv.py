#!/usr/bin/env python3
"""
to_kv module
"""
from typing import Union, Tuple


def to_kv(k: str,  v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple of string and int or float"""
    return (k, float(v ** 2))
