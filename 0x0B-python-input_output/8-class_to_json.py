#!/usr/bin/python3
"""Module containing function that serializes an object

"""
import json


def class_to_json(obj):
    """Serializes an object

    """
    return json.dumps(obj.__dict__)
