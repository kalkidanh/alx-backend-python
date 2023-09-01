#!/usr/bin/env python3
""" An async_comprehension coroutine that takes no argument."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random numbers using an async
    comprehension over async_generator, then return the 10 random numbers
    """
    return [i async for i in async_generator()]
