#!/usr/bin/python3

"""102-square.py: File for the Square class"""


class Square:
    """Square: Square class"""

    def __init__(self, size=0):
        """__init__: Init method"""
        self.size = size

    def __eq__(self, other):
        """__eq__: Equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """__ne__: Not equal"""
        return self.area() != other.area()

    def __lt__(self, other):
        """__lt__: Less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """__le__: Less than or equal"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """__gt__: Greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """__ge__: Greater than or equal"""
        return self.area() >= other.area()

    def area(self):
        """area: Return the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """size: Size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size: Size setter"""
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
