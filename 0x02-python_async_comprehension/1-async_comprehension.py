#!/usr/bin/env python3
"""
coroutine will collect 10 random numbers using an
async comprehensing over async_generator return the 10 random numbers.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return 10 random numbers"""
    random_list = [number async for number in async_generator()]
    return random_list
