#!/usr/bin/python3
"""A module containing function that reads a file.

"""


def read_file(filename=""):
    """Reads a file and prints its content to stdout.

    """
    with open(filename, encoding="utf-8") as a_file:
        for line in a_file:
            print(line, end="")
