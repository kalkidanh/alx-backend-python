#!/usr/bin/env python3
""" A coroutine that will execute async_comprehension in paralell."""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures the runtime."""
    time_strt = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         )
    time_stp = time.perf_counter()
    return (time_stp - time_strt)
