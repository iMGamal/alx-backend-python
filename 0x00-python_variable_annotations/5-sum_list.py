#!/usr/bin/env python3
"""There is no module here."""


def sum_list(input_list: list[float]) -> float:
    """Return sum of list as a float."""
    total: float = 0.0
    for i in range(len(input_list)):
        total += input_list[i]
    return total
