#!/usr/bin/env python3
""" A type-annotated function - sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sum of list of float values

    Args:
          input_list (float): a floating point number

      Returns:
          float: The sum of all floating point values
    """
    return sum(input_list)
