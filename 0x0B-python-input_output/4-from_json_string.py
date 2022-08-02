#!/usr/bin/python3
"""A module containing function that converts JSON string to an object

"""
import json


def from_json_string(my_str):
    """Deserializes a JSON string

    """
    return json.loads(my_str)
