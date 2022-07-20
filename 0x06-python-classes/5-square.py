#!/usr/bin/python3
"""A module containing a Square class.

"""
class Square:
    """Square class.

    """
    def __init__(self, size=0):
        """init method of the class.

        Args:
            size (int): Width of the square.

        """
        self.size = size

    @property
    def size(self):
        """int: size of the square.

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
        """area method of the Square class.

        Returns:
            int: area of the square.

        """
        return self.__size * self.__size

    def my_print(self):
        """my_print method of the Square class.

        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
