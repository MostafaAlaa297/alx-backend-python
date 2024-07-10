#!/usr/bin/env python3

"""
async_generator module
"""
import asyncio
import random


async def async_generator() -> float:
    """Get rand int from yield after 1 second for 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

