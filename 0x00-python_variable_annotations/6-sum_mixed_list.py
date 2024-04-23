#!/usr/bin/env python3
'''A Python script containing a function to calculate
the sum of a mixed list of integers and floats.'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Calculates the sum of a mixed list of integers and floats.

    Parameters:
        mxd_lst (List[Union[int, float]]): A list containing a mixture
        of integers and floats.

    Returns:
        float: The sum of all elements in the mixed list as a float.

    This function takes a mixed list of integers and floats as input
    and returns the sum of all elements in the list as a float using
    the Python's built-in sum() function to perform the summation.
    '''
    return float(sum(mxd_lst))