#!/usr/bin/python3

"""This module defines a Square class"""

import math


class _MagicClass:
    """This class defines a circle by the radius"""

    def __init__(self, radius=0):
        """Initialize a new MagicClass"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area of a circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of a circle"""
        return 2 * math.pi * self.__radius
