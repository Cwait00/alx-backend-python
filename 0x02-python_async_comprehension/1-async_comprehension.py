#!/usr/bin/env python3


"""
1-async_comprehension module
"""


import asyncio
from typing import List
import random


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension.

    Returns:
        List[float]: A list of 10 random numbers.
    """

    return [await asyncio.sleep(0, random.uniform(0, 10)) for _ in range(10)]


# Add two blank lines at the end of the file # noqa
