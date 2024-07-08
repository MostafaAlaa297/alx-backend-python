#!/usr/bin/env python3
"""
element_length module
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns element length"""
    return [(i, len(i)) for i in lst]
