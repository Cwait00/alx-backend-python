#!/usr/bin/env python3


"""
This module provides a function to compute the length of elements in an iterable of sequences.
"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element from the input list
    along with its length.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        an element from the input list along with its length.
    """
    return [(i, len(i)) for i in lst]
