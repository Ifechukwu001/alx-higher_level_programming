#!/usr/bin/python3
"""A module containing a Square class.

"""


class Square:
    """Square class with setter to private feild.

    Attributes:
        size (int): Width of the square.

    """
    def __init__(self, size=0):
        """ init method of the class.

        Args:
            size (int): Width of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
