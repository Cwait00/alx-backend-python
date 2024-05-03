#!/usr/bin/env python3


"""
This module provides a function to safely retrieve a value from a dictionary.
"""


import typing

T = typing.TypeVar('T')

def safely_get_value(dct: typing.Mapping, key: typing.Any, default: typing.Union[T, None] = None) -> typing.Union[typing.Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (typing.Mapping): The input dictionary.
        key (typing.Any): The key to retrieve the value for.
        default (typing.Union[T, None], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        typing.Union[typing.Any, T]: The value corresponding to the key, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
