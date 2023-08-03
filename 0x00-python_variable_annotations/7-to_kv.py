#!/usr/bin/env python3
"""Take a string and float return tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Returns a tuple with string and square of float"""
    return (k, float(v**2))
