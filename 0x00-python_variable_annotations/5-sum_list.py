#!/usr/bin/env python3
"""
sum_list module
"""
from typing import List


def sum_list(input_list: List[float])-> float:
    """return the sum of a list"""
    res = 0
    for num in input_list:
        res += num
    return res
