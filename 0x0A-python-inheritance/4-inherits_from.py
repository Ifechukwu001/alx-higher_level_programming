#!/usr/bin/python3
"""A module containing function that checks \
if an object is a subclass of a class.

"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a subclass of a super class.

    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    return False
