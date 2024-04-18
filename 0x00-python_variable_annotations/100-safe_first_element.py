#!/usr/bin/env python3
''' Module '''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Commnent '''
    if lst:
        return lst[0]
    else:
        return None
