#!/usr/bin/python3
"""Module for append_write method."""


def append_write(filename="", text=""):
    """Method for appending text to a file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        The number of characters appended.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
