#!/usr/bin/python3


"""Module for Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Constructor.

            Args:
                size (int): size of square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area of the square."""
        return self.__size ** 2
