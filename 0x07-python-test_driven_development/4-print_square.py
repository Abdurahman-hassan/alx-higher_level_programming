#!/usr/bin/python3

"""
This module contains a function that prints a square with the character #.
"""


def print_square(size):
    """
    This function prints a square with the character #.

    Args:
        size (int): size of the square

    Raises:
        TypeError: If the input `size` is not an integer.
        ValueError: If the input `size` is less than 0.

    Return:
        None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
