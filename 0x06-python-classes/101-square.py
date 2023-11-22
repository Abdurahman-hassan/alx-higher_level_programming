#!/usr/bin/python3

"""Square class"""


class Square:
    """Square class with private attribute size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square with size and position"""
        self.size = size
        self.position = position

    def __str__(self):
        """Returns string representation of Square"""
        if self.__size == 0:
            return ""
        else:
            return "\n" * self.__position[1] + \
                (" " * self.__position[0] + "#" * self.__size + "\n") * \
                (self.__size - 1) + " " * self.__position[0] + "#" * \
                self.__size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns area of Square"""
        return self.__size ** 2

    def my_print(self):
        """Prints Square to stdout with #"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print(
                (
                    " " * self.__position[0] + "#" * self.__size + "\n"
                ) * (self.__size - 1)
                + " " * self.__position[0]
                + "#" * self.__size
            )
