#!/usr/bin/env python3
""" Measuring the total execution time for wait_n."""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """A function that measures the total execution time

    Args:
        n (int): an integer number
        max_delay (int): maximum delay to wait for

    Returns:
        float: total execution time
    """
    start = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end = time.perf_counter()

    time_tot = end - start

    return time_tot / n
