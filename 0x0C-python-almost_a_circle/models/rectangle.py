#!/usr/bin/python3

"""Defines a Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.
        Args:
            width (int): The width of the Rectangle instance.
            height (int): The height of the Rectangle instance.
            x (int): The x coordinate of the Rectangle instance.
            y (int): The y coordinate of the Rectangle instance.
            id (int): The identity of the Rectangle instance.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance to stdout."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """Updates the Rectangle instance by assigning an argument to each
        attribute.
        Args:
            args (tuple): A tuple of arguments.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represents height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            kwargs (dict): A dictionary of arguments.
                - Only key/value arguments are accepted
        """
        attr_order = ['id', 'width', 'height', 'x', 'y']

        # Update using args
        if args:
            for attr, value in zip(attr_order, args):
                setattr(self, attr, value)

        # Update using kwargs
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr_order:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle instance."""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    def __str__(self):
        """Returns the string representation of a Rectangle instance."""
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.x, self.y,
            self.width, self.height)
