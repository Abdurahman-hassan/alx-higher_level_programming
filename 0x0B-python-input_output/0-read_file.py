#!/usr/bin/python3
"""Module for read_file method."""


def read_file(filename=""):
    """Method for reading a file.

        Args:
            filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
