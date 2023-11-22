#!/usr/bin/python3
"""
Defines a MagicClass that represents a circle and provides
methods to calculate its area and circumference.
"""

from math import pi


class MagicClass:
    """
    A class representing a circle with methods to calculate
    its area and circumference.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with a specified radius.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If the provided radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return (pi * (self.__radius ** 2))

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return (2 * pi * self.__radius)
