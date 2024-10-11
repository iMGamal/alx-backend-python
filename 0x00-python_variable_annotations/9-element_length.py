#!/usr/bin/env python3
"""This is the module for our program."""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Return length of an object."""
    return [(i, len(i)) for i in lst]
