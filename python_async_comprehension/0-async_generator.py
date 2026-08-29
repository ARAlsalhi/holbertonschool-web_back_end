#!/usr/bin/env python3
"""This module provides an asynchronous random-number generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random floats with a one-second asynchronous delay"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
