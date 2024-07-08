#!/usr/bin/env python3
"""
sum_mixed_list module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of a mixed list"""
    res = 0
    for num in mxd_lst:
        res += num
    return res
