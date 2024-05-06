#!/usr/bin/env python3

import asyncio
from typing import List
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Call wait_random n times with max_delay and return a sorted list of delays.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for each call to wait_random.

    Returns:
        List[float]: A sorted list of delays.

    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)

# Example usage
if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
