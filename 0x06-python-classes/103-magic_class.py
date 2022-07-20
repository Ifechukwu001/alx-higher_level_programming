#!/usr/bin/python3
"""A module containing a MagicClass class

"""
import math


class MagicClass:
    """A MagicClass class

    """
    def __init__(self, radius=0):
        """init method.

        Args:
            radius (int or float): Radius of the circle.

        Raises:
            TypeError: if radius is not a number.

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area method of class.

        Returns:
            int: area of a circle.

        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """circumference method of class.

        Returns:
            int: Circumference of a circle.

        """
        return (2 * math.pi) * self.__radius
