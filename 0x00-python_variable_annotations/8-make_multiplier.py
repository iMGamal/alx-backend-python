#!/usr/bin/env python3
"""This is the module of our program."""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Return the multiplication of a float."""
    def multiply(value: float) -> float:
        """Return a float."""
        return value * multiplier
    return multiply
