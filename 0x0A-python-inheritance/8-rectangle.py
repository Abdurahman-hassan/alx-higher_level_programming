#!/usr/bin/python3


"""Module for BaseGeometry class."""


class BaseGeometry:
    """
    A base class for geometry-related operations.
    """

    def __init__(self, width, height):
        """
        Initializes a BaseGeometry object.

        Args:
            width (int): The width of the object.
            height (int): The height of the object.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Placeholder method for calculating the area of a geometry.
        This method is meant to be overridden in derived classes.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def __str__(self):
        """
        Returns a string representation of a BaseGeometry object.
        """

        return f"[BaseGeometry] {self.__width}/{self.__height}"
