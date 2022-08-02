#!/usr/bin/python3
"""Module containing function that serializes an object

"""


def class_to_json(obj):
    """Serializes an object

    """
    return obj.__dict__
