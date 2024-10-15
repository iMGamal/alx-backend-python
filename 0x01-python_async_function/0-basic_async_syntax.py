#!/usr/bin/env python3
"""There is the module for our pogram."""
from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Return the float."""
    random_delay = uniform(0, max_delay)
    await sleep(random_delay)
    return random_delay
