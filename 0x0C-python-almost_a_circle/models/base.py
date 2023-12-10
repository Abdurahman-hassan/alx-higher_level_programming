#!/usr/bin/python3
"""Defines a base class for all other classes in this project."""


class Base:
    """
        Base class for all other classes in this project
        Attributes:
            __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize a new Base object
            Args:
                id (int): The identity of the new Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
