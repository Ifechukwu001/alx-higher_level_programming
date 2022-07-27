#!/usr/bin/python3
"""A module containing a function that prints a square.

>>> print_square(2)
##
##

"""


def print_square(size):
    """A function that prints a square.

    Args:
        size (int): Length of the square.

    Raises:
        TypeError: if size is not an integer or is a float less than zero.
        ValueError: if size is less than zero.

    """
    if type(size) is not int:
        if type(size) is float and size >= 0:
            size = int(size)
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
