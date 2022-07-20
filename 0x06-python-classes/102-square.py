#!/usr/bin/python3
"""A module containing a Square class

"""


class Square:
    """A Square class

    """
    def __init__(self, size=0):
        """init method of the class.

        Args:
            size (int): Width of the square.

        """
        self.size = size

    @property
    def size(self):
        """int: Size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.

        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area method of the class.

        Returns:
            int: area of the square.

        """
        return self.__size * self.__size

    def __eq__(self, other):
        """implements '=='

        Returns:
            bool: True or False

        """
        return self.__size == other.size

    def __ne__(self, other):
        """implements '!='

        Returns:
            bool: True or False

        """
        return self.__size != other.size

    def __ge__(self, other):
        """implements '>='

        Returns:
            bool: True or False

        """
        return self.__size >= other.size

    def __le__(self, other):
        """implements '<='

        Returns:
            bool: True or False

        """
        return self.__size <= other.size

    def __gt__(self, other):
        """implements '>'

        Returns:
            bool: True or False

        """
        return self.__size > other.size

    def __lt__(self, other):
        """implements '<'

        Returns:
            bool: True or False

        """
        return self.__size < other.size
