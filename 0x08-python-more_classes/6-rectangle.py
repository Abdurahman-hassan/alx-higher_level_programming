#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle
    Attributes:
        number_of_instances(int): Number of instances created.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initilization method for Rectangle.
        Args:
            width(int): Size of the width of the rectangle.
            height(int): Size of the height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Method to recover the value of width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set the value of width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Method to recover the value of height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set the value of height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Method that returns a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Method that returns a string representation of the rectangle for
        reproduction"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method that deletes an instance of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
