#!/usr/bin/python3
"""A module containing function that checks if an object is of a class

"""


def is_same_class(obj, a_class):
    """Checks if an object is of a type a_class

    """
    return type(obj) is a_class
