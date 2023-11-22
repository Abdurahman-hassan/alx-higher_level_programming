#!/usr/bin/python3

import math


class MagicClass:
    """MagicClass: Magic class"""

    def __init__(self, radius=0):
        """__init__: Init method"""
        self.__radius = 0
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area: Return the area of the circle"""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """circumference: Return the circumference of the circle"""
        return 2 * math.pi * self.__radius
