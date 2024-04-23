#!/usr/bin/env python3
'''A module containing a function to calculate the length of elements
in an iterable of sequences.
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Calculates the length of elements in an iterable of sequences and
    returns a list of tuples, each containing the original element and its length.
    
    Parameters:
        - lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
        - List[Tuple[Sequence, int]]: A list of tuples, each containing the
        original element and its length.
    '''
    return [(i, len(i)) for i in lst]