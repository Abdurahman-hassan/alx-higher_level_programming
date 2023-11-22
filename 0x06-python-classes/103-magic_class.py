import math

""" MagicClass is used for performing operations related to a circle."""


class MagicClass:
    """
    MagicClass is used for performing operations related to a circle.

    Attributes:
    __radius (float or int): The radius of the circle.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass object with a radius.

        Args:
        radius (float or int, optional): The radius of circle. Defaults to 0.

        Raises:
        TypeError: If the radius is not an integer or float.
        """
        self.__radius = 0
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
        float: The area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
        float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
