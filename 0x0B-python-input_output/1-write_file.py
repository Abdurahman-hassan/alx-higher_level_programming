#!/usr/bin/python3
"""Module for write_file method."""


def write_file(filename="", text=""):
    """Method for writing to a file.

        Args:
            filename (str): The name of the file to write to.
            text (str): The text to write to the file.

        Returns:
            The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
