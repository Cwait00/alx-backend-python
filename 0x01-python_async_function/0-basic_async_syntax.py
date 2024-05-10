#!/usr/bin/env python3


"""
Module to demonstrate basic asynchronous syntax.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay (inclusive) seconds and
    return the delay.

    :param max_delay: The maximum delay in seconds. Defaults to 10.
    :return: A float value representing the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    asyncio.run(wait_random())
