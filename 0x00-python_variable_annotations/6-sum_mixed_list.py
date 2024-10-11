#!/usr/bin/env python3
"""There is no module here."""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Return sum of integer and float as a float."""
    return sum(mxd_lst)
