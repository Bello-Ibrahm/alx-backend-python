#!/usr/bin/env python3
'''A simple function to calculate the sum of a list of floats.

This script defines a function `sum_list` that takes a list of floats
as input and returns the sum of all the elements in the list.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Calculate the sum of a list of floats.

    Parameters:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of all elements in the input list.
    '''
    return float(sum(input_list))