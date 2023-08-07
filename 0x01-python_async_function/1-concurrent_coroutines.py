#!/usr/bin/env python3
"""
write an async routine that takes 2 arguments(n and max_delay)
wait_n should return the list of all the delays (float values)
"""
import asyncio
import random
from heapq import nsmallest
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    delays_list = []
    for i in range(n):
        delays_list.append(await wait_random(max_delay))
    return nsmallest(n, delays_list)
