#!/usr/bin/env python3
'''A module containing a function to zoom in on an array by
duplicating its elements multiple times.
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Zooms in on an array by duplicating its elements multiple times.

    Parameters:
        - lst (Tuple): The input array.
        - factor (int): The zoom factor (default is 2).

    Returns:
        - List: The zoomed-in array.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)