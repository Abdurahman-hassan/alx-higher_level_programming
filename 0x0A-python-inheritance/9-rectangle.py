#!/usr/bin/python3
"""Module for BaseGeometry class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A base class for geometry-related operations.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle geometry.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Calculates the area of a Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of a Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
