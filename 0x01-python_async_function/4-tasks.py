#!/usr/bin/env python3

"""
Module: 4-tasks

This module provides a function task_wait_n to create asyncio tasks for wait_random coroutine.
"""

import asyncio
from typing import List
from random import uniform

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Call task_wait_random n times with max_delay and return a sorted list of delays.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay for each call to task_wait_random.

    Returns:
        List[float]: A sorted list of delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)

# Example usage
if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
