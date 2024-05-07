#!/usr/bin/env python3

import sys
sys.path.append('/root/alx-backend-python/0x02-python_async_comprehension')

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    """
    This coroutine prints the values yielded by the async_generator coroutine.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
