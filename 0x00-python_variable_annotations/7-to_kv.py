#!/usr/bin/env python3
'''A script containing a function to convert a key-value pair
with a numerical value into a new key-value pair with the
original key and the square of the numerical value.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key-value pair with a numerical value into a new
    key-value pair with the original key and the square of the numerical value.

    Parameters:
        - k (str): The key.
        - v (Union[int, float]): The numerical value.

    Returns:
        - Tuple[str, float]: A tuple containing the original key and the square of the numerical value.
    '''
    return (k, float(v**2))