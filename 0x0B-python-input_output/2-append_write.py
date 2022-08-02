#!/usr/bin/python3
"""A module containing function that appends text to a file

"""


def append_write(filename="", text=""):
    """ Appends text to a file

    """
    char_num = 0
    with open(filename, mode="a", encoding="utf-8") as a_file:
        char_num = a_file.write(text)
    return char_num
