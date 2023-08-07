#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a float delay"""
    delays = random.uniform(0, max_delay)
    await asyncio.sleep(delays)
    return delays
