#!/usr/bin/env python3
"""This is the module for our program."""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[Any, T]) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
