#!/usr/bin/env python3
"""
concurrent_coroutines module
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """returns the list of all the delays"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
