#!/usr/bin/env python3
""" A type-annotated function - sum_mixed_list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sum as a floating point number

    Args:
        mxd_lst (List[Union[int, float]]): list of integers and floats

    Returns:
        float: The sum of all values as a float.
    """
    return sum(mxd_lst)
