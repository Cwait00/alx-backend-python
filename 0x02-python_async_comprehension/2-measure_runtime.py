#!/usr/bin/env python3

"""
2-measure_runtime module
"""

import asyncio
from typing import List
from time import perf_counter
from asyncio import Task

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times
    in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()

    # Execute async_comprehension four times in parallel
    awaitables = [async_comprehension() for _ in range(4)]
    results = await asyncio.gather(*awaitables)

    end_time = perf_counter()
    return end_time - start_time

if __name__ == "__main__":
    # Run the main coroutine and print the result
    print(asyncio.run(measure_runtime()))

# empty line added at the end
