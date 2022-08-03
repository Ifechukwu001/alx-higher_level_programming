#!/usr/bin/python3
"""Module containing function that appends text after a line.

"""


def append_after(filename="", search_string="", new_string=""):
    """Appends text after lines

    """
    final = []
    with open(filename, mode="r", encoding="utf-8") as myfile:
        lines = myfile.readlines()
        for line in lines:
            final.append(line)
            if search_string in line:
                final.append(new_string)

    with open(filename, mode="w", encoding="utf-8") as myfile:
        for line in final:
            myfile.write(line)
