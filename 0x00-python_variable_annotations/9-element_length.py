#!/usr/bin/env python3
"""This is the module for our program."""
from typing import List, Sequence, Tuple, Iterable


type_lst = Iterable[Sequence]


def element_length(lst: type_lst) -> List[Tuple[Sequence, int]]:
    """Return length of an object."""
    return [(i, len(i)) for i in lst]
