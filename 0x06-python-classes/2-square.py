#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    """This class implements a Square"""

    def __init__(self, size=0):
        """Method __init initializes a private instance attribute
        size with option (self, size=0) and raise some exceptions"""
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method area returns the square area"""
        return self.__size ** 2
