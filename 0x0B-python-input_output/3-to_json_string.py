#!/usr/bin/python3
"""A module containing function that serializes an object.

"""
import json


def to_json_string(my_obj):
    """ Serializes an object to JSON

    """
    return json.dumps(my_obj)
