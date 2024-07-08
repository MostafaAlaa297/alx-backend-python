#!/usr/bin/env python3
"""
element_length module
"""
from typing import Iterable, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    """returns element length"""
    return [(i, len(i)) for i in lst]
