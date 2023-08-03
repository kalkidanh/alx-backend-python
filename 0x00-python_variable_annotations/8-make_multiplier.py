#!/usr/bin/env python3
""" A type-annotated function make_multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Multiply a floating point number by a multiplier

    Args:
        multiplier (float): A floating point multiplier

    Returns:
        Callable[[float], float]: Function that multiplies
        a floating point number by a multiplier
    """
    def multiply(n: float):
        return n * multiplier
    return multiply
