#!/usr/bin/python3
"""A module containing function that serializes an object and saves it to a file

"""
import json


def save_to_json_file(my_obj, filename):
    """ Serializes an object and saves it to a file.

    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
