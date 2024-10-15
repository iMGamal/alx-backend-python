#!/usr/bin/env python3
"""This is the module for our program."""
import asyncio
import random


async def async_generator():
    """Generate async."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == "__main__":
    asyncio.run(async_generator())
