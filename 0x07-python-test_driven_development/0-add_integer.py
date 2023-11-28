#!/usr/bin/python3

"""

Module for add_integer method.

"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
