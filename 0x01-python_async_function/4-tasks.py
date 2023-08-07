#!/usr/bin/env python3
"""
Function task_wait_n that calls task_wait_random
"""

import asyncio
from heapq import nsmallest
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    ranndom_list = await asyncio.gather(*tasks)
    return nsmallest(n, ranndom_list)
