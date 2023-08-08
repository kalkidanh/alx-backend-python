#!/usr/bin/env python3
""" An asynchronous coroutine that waits for a random delay."""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Function that waits for a random delay between 0 and max_delay

    Args:
        max_delay (int, optional): an integer number.

    Returns:
        float: a random delay between 0 and 10.
    """
    delay_rand = random.uniform(0, max_delay)
    await asyncio.sleep(delay_rand)
    return delay_rand
