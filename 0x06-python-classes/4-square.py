#!/usr/bin/python3
"""A module containing a Square class.

"""
class Square:
    """Square class with setter and getter to private feild.

    """
    def __init__(self, size=0):
        """init method of the class.

        Args:
            size (int): Width of the square.

        """
        self.size = size

    @property
    def size(self):
        """int: a getter for the size attribute.

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
            int: Area of the square.

        """
        return self.__size * self.__size
