#!/usr/bin/env python3
'''This is task 0's module.'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''This generates sequence of 10 numbers.'''

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
