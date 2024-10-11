#!/usr/bin/env python3
"""This is the module for our program."""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return a NoneType."""
    if lst:
        return lst[0]
    else:
        return None
