#!/usr/bin/env python3
"""
Coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it"""
    start_time: float = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time: float = perf_counter()
    total_time = end_time - start_time
    return total_time
