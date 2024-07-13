#!/usr/bin/env python3

"""
async_comprehension module
"""
import asyncio
import time
from typing import AsyncGenerator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that will execute async_comprehension four
    times in parallel using asyncio.gather
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()

    total = end - start

    return total
