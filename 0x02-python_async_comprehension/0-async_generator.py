#!/usr/bin/env python3


import asyncio
import random

async def async_generator():
    """
    This coroutine generates a sequence of random numbers.

    It asynchronously waits 1 second between each number and yields
    a random number between 0 and 10.
    """
    random.seed(42)  # Set a fixed seed for reproducibility
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
