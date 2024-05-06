#!/usr/bin/env python3


"""
Module: 3-tasks

This module provides a function task_wait_random to create an asyncio task for wait_random coroutine.
"""

import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random(max_delay).
    
    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: An asyncio task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

# Example usage
if __name__ == "__main__":
    async def test(max_delay: int) -> None:
        """
        Test function to demonstrate the usage of task_wait_random.
        """
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
