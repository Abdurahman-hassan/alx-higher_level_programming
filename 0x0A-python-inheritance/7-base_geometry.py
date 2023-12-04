#!/usr/bin/python3


"""Module for BaseGeometry class."""


class BaseGeometry:
    """The BaseGeometry class."""

    def area(self):
        """Raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
