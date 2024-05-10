#!/usr/bin/env python3


"""
Module: 2-measure_runtime
"""


import asyncio
from typing import Callable
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of wait_n(n, max_delay).

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each call to wait_n.

    Returns:
        float: The average execution time per call to wait_n.
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
