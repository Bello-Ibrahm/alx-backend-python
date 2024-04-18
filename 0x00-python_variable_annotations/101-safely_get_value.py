#!/usr/bin/env python3
''' Module '''
from typing import Any, Union, Mapping, TypeVar


T = TypeVar('T')
Def = Union[T, None]
Res = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    ''' Comment '''
    if key in dct:
        return dct[key]
    else:
        return default
