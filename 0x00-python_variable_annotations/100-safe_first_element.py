#!/usr/bin/env python3
'''A module containing a function to safely retrieve the
first element from a sequence.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Safely retrieves the first element from a sequence.

    Parameters:
        - lst (Sequence[Any]): The sequence from which to retrieve the first element.

    Returns:
        - Union[Any, None]: The first element of the sequence if it exists, otherwise None.
    '''
    if lst:
        return lst[0]
    else:
        return None