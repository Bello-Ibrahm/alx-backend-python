#!/usr/bin/env python3
'''A module containing a function for safely retrieving a value
from a dictionary given a key.
'''
from typing import Any, Union, Mapping, TypeVar


T = TypeVar('T')
Def = Union[T, None]
Res = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Safely retrieves a value from a dictionary given a key, with an optional
    default value if the key is not found.

    Parameters:
        - dct (Mapping): The dictionary to retrieve the value from.
        - key (Any): The key to search for in the dictionary.
        - default (Def): Optional. The default value to return if the key
        is not found in the dictionary. Defaults to None.

    Returns:
        - Res: The value associated with the key in the dictionary, or the default value
        if the key is not found.
    '''
    if key in dct:
        return dct[key]
    else:
        return default