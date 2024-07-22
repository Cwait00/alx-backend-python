#!/usr/bin/env python3

"""
1-async_comprehension module
"""

import asyncio
from typing import List
import random


async def generate_random_numbers() -> List[float]:
    """
    Generate 10 random numbers asynchronously.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(0)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [number async for number in generate_random_numbers()]

# Add two blank lines at the end of the file # noqa
