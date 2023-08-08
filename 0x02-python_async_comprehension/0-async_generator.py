#!/usr/bin/env python3
"""
Coroutine will loop 10 times, each time asynchronously wait 1s
"""

import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
