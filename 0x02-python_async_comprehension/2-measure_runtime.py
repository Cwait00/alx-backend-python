#!/usr/bin/env python3

"""
2-measure_runtime module
"""

import asyncio
from time import time


async def async_comprehension(n):
    """Asynchronous comprehension."""
    print(f'Starting {n}')
    await asyncio.sleep(5)
    print(f'Ending {n}')


async def measure_runtime():
    """Measure runtime."""
    start = time()
    await asyncio.gather(
        async_comprehension(1),
        async_comprehension(2),
        async_comprehension(3),
        async_comprehension(4),
    )
    end = time()
    return end - start
