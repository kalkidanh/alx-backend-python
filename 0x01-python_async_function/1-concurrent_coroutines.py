#!/usr/bin/env python3
""" Executing multiple coroutines."""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ The list of all the delays.

    Args:
        n (int): an integer number
        max_delay (int): delay to wait for

    Returns:
        List[float]: list of the delays
    """
    delay = []
    for i in range(n):
        delay.append(wait_random(max_delay))

    delay_list = []
    for i in asyncio.as_completed(delay):
        delay_list.append(await i)

    return delay_list
