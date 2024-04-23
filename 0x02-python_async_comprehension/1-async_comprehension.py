#!/usr/bin/env python3
'''Task 1's module.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Comments.
    '''
    return [randNum async for randNum in async_generator()]
