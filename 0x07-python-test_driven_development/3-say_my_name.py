#!/usr/bin/python3
"""A module containing funtion that prints a name.

>>> say_my_name("John", "Smith")
My name is John Smith

"""


def say_my_name(first_name="", last_name=""):
    """A fuction that prints the full name of a person.

    Args:
        first_name (str): First name.
        last_name (str): Last name.

    Raises:
        TypeError: if first_name or last_name is not a string.

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
