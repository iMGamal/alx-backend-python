#!/usr/bin/env python3
"""This is the module for our program."""
import asyncio
import typing


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.Generator[float, None, None]:
    """Yield a list comprehension."""
    for i in range(10):
        result = [i async for i in async_generator()]
        return result


if __name__ == "__main__":
    asyncio.run(async_comprehension())
