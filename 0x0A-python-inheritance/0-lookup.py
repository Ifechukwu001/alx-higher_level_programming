#!/usr/bin/python3
"""A module containing function returns a \
list of all attributes of an object

"""


def lookup(obj):
    """Finds all attributes of an object.

    Returns:
        :obj:`list`: List of all attributes of the object(obj).

    """
    return dir(obj)
