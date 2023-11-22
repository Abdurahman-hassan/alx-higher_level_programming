#!/usr/bin/python3

"""Module 3-square"""


class Square:
    """defines class Square with private attribute __size"""

    def __init__(self, size=0):
        """initializes Square with size attribute"""
        self.__size = size

    def area(self):
        """returns area of Square instance"""
        return self.__size ** 2
