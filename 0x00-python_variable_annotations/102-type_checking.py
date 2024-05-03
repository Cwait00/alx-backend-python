#!/usr/bin/env python3


"""
This script defines a function to zoom in on the elements of a tuple by repeating each element 'factor' times.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """
    Zooms in on the elements of a tuple by repeating each element 'factor' times.

    Args:
        lst (Tuple[int]): The input tuple.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        List[int]: The zoomed-in list.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
