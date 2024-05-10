#!/usr/bin/env python3

"""
2-measure_runtime module
"""


import asyncio
import time

from typing import List, AsyncIterator


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
    Measure the runtime of executing async_comprehension four
    times in parallel.
    """

    start_time = time.monotonic()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.monotonic()
    total_runtime = end_time - start_time
    return total_runtime


if __name__ == "__main__":
    runtime = asyncio.run(measure_runtime())

    if runtime <= 11:
        print(
            "Function returns a runtime that is within 10 seconds plus "
            "a 10% overhead"
        )

    print(
        asyncio.run(measure_runtime()) == asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
        )
    )

    print(
        isinstance(runtime, float)
    )

    print(
        all(func.__doc__ for func in (
            async_generator,
            async_comprehension,
            measure_runtime
        ))
    )
