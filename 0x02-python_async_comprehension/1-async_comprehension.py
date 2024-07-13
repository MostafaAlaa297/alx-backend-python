#!/usr/bin/env python3

"""
async_comprehension module
"""
import asyncio
import random
from typing import AsyncGenerator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[float, None]:
    """Collects 10 random numbers using async comprehension."""
    return [value async for value in async_generator()]
