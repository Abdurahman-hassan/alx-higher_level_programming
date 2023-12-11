#!/usr/bin/python3

"""Defines a Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

        Args:
            size (int): The size of the Square instance.
            x (int): The x coordinate of the Square instance.
            y (int): The y coordinate of the Square instance.
            id (int): The identity of the Square instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of a Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Gets the size attribute of a Square instance."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size attribute of a Square instance.

        args:
            value (int): The value to set
            the size attribute to.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates a Square instance.
        """
        attrs = ["id", "size", "x", "y"]
        if args:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

        # Update using args

    def to_dictionary(self):
        """Returns the dictionary representation of a Square instance."""
        return {'id': getattr(self, "id"),
                'size': getattr(self, "size"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
