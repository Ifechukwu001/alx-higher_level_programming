#!/usr/bin/python3
""" A module containing function that writes text to a file

"""


def write_file(filename="", text=""):
    """ Writes text to a file

    """
    char_num = 0
    with open(filename, mode="w", encoding="utf-8") as a_file:
        char_num = a_file.write(text)
    return char_num
