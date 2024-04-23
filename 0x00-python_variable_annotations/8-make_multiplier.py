#!/usr/bin/env python3
'''A script containing a function to create a multiplier function.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates and returns a multiplier function that multiplies its input
    by a specified multiplier.

    Parameters:
        - multiplier (float): The multiplier value.

    Returns:
        - Callable[[float], float]: A function that multiplies its input
        by the specified multiplier.
    '''
    return lambda i: i * multiplier