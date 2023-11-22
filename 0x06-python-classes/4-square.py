#!/usr/bin/python3

"""This module creates a class Square"""


class Square:
    """Square class
    """

    def __init__(self, size=0):
        """Initializes instance of Square
        Args:
            size (int): size of Square
        """
        self.size = size

    @property
    def size(self):
        """Getter for size
        Returns:
            size of Square instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size
        Args:
            value (int): size of Square instance
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("ize must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of Square instance
        Returns:
            Area of Square instance
        """
        return self.__size ** 2

    def my_print(self):
        """Prints Square instance with '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
