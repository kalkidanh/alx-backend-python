#!/usr/bin/env python3
""" Using mypy to validate the code."""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Type checking

    Args:
        lst (Tuple): List of the Tuple
        factor (int, optional): _description_. Defaults to 2.

    Returns:
        List: List of all values with the appropriate type
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
