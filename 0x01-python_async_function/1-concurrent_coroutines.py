#!/usr/bin/env python3
"""These are the modules for our program."""
import asyncio
from typing import List
from 1-concurrent_coroutines import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Create a list of tasks by spawning wait_random n times."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Use asyncio.gather to execute all tasks concurrently and return their results
    delays = []
    
    for task in asyncio.as_completed(tasks):  # as_completed returns tasks in the order they are completed
        delay = await task
        delays.append(delay)  # Add completed delay to the list

    return delays
