#!/usr/bin/env python3

"""
2-measure_runtime module
"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension
    four times sequentially.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.perf_counter()  # Record start time

    # Execute async_comprehension four times sequentially
    await async_comprehension()
    await async_comprehension()
    await async_comprehension()
    await async_comprehension()

    end_time = time.perf_counter()  # Record end time

    total_runtime = end_time - start_time
    return total_runtime

if __name__ == "__main__":
    runtime = asyncio.run(measure_runtime())
    print(f"Total runtime: {runtime:.2f} seconds")
