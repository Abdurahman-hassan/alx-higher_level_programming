#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            age (int): The age.

        Raises:
            TypeError: If `age` is not an integer.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.

        If `attrs` is a list of strings, only attribute names contained
        in the list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Args:
            attrs (list): A list of attribute names.

        Returns:
            dict: A dictionary representation of the Student.

        """
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            # This line checks whether attrs
            # is a list and all elements in the list are strings.
            # If this condition is true
            # the method proceeds to generate a dictionary.
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        #  If attrs is not a list of strings,
        #  this line returns a shallow copy of the entire
        return self.__dict__.copy()

        # or
        # if isinstance(attrs, list):
        #         return {k: v for k, v in self.__dict__.items() if k in attrs}
        #     elif isinstance(attrs, dict):
        #         return {k: attrs[k](v) if k in attrs else v
        #         for k, v in self.__dict__.items()}
        #     elif attrs is None:
        #         return self.__dict__.copy()
        #     else:
        #         return {}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): A dictionary representation of a Student.

        """
        self.__dict__.update(json)
