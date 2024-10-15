#!/usr/bin/env python3
"""There is the module for our pogram."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return the float."""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


if __name__ == "__main__":
    asyncio.run(wait_random())
