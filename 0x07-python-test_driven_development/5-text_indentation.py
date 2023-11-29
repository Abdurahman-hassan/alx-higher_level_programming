#!/usr/bin/python3

"""
Module for text_indentation method.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in [".", "?", ":"]:
        lines = [line.strip(" ") for line in text.split(delim)]
        text = f"{delim}\n\n".join(lines)

    print(text, end="")
