#!/usr/bin/env python3
"""Takes a list mxd_lst of integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns a float"""
    return sum(mxd_lst)
