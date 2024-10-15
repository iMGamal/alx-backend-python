#!/usr/bin/env python3
"""These are the modules for our program."""
import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Return a list of wait time."""
    wait_list: typing.List[float] = []
    for i in range(n):
        result = await wait_random(max_delay)
        wait_list.append(result)
    return sorted(wait_list)


if __name__ == "__main__":
    asyncio.run(wait_n())
