#!/usr/bin/env python3
"""Take a float multiplier as argument"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiplier_fn(num: float) -> float:
        return num * multiplier
    return multiplier_fn
