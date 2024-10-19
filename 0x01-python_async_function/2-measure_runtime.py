#!/usr/bin/env python3
"""This is the module for our program."""
import asyncio
import time
import random


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Return total time."""
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    finish: float = time.time()
    total_time: float = finish - start
    return total_time / n
