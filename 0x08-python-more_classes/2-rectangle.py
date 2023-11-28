#!/usr/bin/python3
"""Module 2-rectangle"""


class Rectangle:
    """Rectangle class defined by width and height"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the width of the rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle instance.
        Args:
            value (int): the width of the rectangle instance.
        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle instance.
        Args:
            value (int): the height of the rectangle instance.
        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the area of the rectangle instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
