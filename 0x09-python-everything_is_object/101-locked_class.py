#!/usr/bin/python3
"""Module containing a LockedClass

"""


class LockedClass:
    """This class can only have one attribute: first_name

    """
    __slots__ = ["first_name"]
