#!/usr/bin/env python3
"""This is the module for our program."""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    return (k, v*v)
