#!/usr/bin/env python3

"""
2-measure_runtime module
"""

import asyncio

from typing import List, AsyncIterator  # Import AsyncIterator


async def async_generator(n: int) -> AsyncIterator[int]:
    """
    Generate an asynchronous generator that yields numbers from 0 to n-1.
    """
    for i in range(n):
        yield i


async def async_comprehension() -> List[int]:
    """
    Collect 10 random numbers using an async comprehension.
    """
    return [number async for number in async_generator(10)]


async def measure_runtime() -> float:
    """
    Measure the runtime of executing async_comprehension four times in parallel.
    """
    # Execute async_comprehension four times in parallel
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = asyncio.get_event_loop().time()

    # Calculate the total runtime
    total_runtime = end_time - start_time

    return total_runtime


if __name__ == "__main__":
    asyncio.run(measure_runtime())
