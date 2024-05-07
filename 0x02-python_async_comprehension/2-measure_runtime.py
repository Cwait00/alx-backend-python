#!/usr/bin/env python3

"""
2-measure_runtime module
"""

import asyncio
from typing import List

async def async_generator(n):
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
    tasks = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    # Flatten the list of lists into a single list
    flattened_tasks = [item for sublist in tasks for item in sublist]

    # Calculate the total runtime
    total_runtime = sum(flattened_tasks) / len(flattened_tasks)

    return total_runtime

# empty line added at the ending
