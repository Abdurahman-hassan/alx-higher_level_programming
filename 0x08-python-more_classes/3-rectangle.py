#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initilization method for Rectangle.
        Args:
            width(int): width of rectangle, defaults to 0
            height(int): height of rectangle, defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set width
        Args:
            value(int): value to set width to
        Raises:
            TypeError: if width is not an int
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method to get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set height
        Args:
            value(int): value to set height to
        Raises:
            TypeError: if height is not an int
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to get area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method to get perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Method to print rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def __repr__(self):
        """Method to print string representation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
