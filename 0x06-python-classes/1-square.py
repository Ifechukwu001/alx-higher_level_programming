#!/usr/bin/python3
"""A module containing a Square class.

"""


class Square:
    """Square class with a private feild.

       Attributes:
           size (int): Width of the square.
    """
    def __init__(self, size):
        """__init__ method of the class.

           Args:
               size (int): Width of the square.
        """
        self.__size = size
