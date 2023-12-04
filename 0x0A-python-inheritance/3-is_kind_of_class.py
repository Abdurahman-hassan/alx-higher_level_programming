#!/usr/bin/python3

"""Defines a function that returns True if the object is an instance of,"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a class that inherits
    from a_class; otherwise return False.
    """
    return isinstance(obj, a_class)
