#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
"""
import asyncio
import random


async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay