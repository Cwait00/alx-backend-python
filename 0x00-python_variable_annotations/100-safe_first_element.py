#!/usr/bin/env python3


"""
This module provides a function to safely retrieve the first element of a sequence.
"""


from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely returns the first element of a sequence or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Optional[Any]: The first element of the sequence, if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
