#!/usr/bin/env python3


"""
This module provides a function to create a multiplier function.
"""


from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the multiplier.
    """
    def multiplier_func(x: float) -> float:
        """
        Multiplies a float by the given multiplier.

        Args:
            x (float): The input float.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return multiplier_func
