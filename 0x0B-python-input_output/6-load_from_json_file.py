#!/usr/bin/python3
"""Module containing function that deserializes a JSON file

"""
import json


def load_from_json_file(filename):
    """Deserializes a JSON FILE

    """
    with open(filename, encoding="utf-8") as a_file:
        obj = json.load(a_file)
    return obj
