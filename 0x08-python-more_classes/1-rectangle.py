#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Init method to initialized a instance.

        Args:
            width (int): Size of the width
            height (int): Size of the height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method getter for width atributte"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method setter for width atributte"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >=0")

        self.__width = value

    @property
    def height(self):
        """Method getter for height atributte"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method setter for height atributte"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >=0")

        self.__height = value
