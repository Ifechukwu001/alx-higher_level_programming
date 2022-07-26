#!/usr/bin/python3
"""A module containing an Integer addition function.

>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """A function that adds two integers together.

    Args:
        a (int): First number.
        b (int): Second number.

    Raises:
        TypeError: if a or b is not an integer or a float.

    Returns:
        int: Sum of a and b.

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
