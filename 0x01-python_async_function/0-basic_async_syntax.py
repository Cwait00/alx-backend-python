#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main():
    result1 = await wait_random()
    result2 = await wait_random(5)
    result3 = await wait_random(15)
    print(result1)
    print(result2)
    print(result3)

# Example usage
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
