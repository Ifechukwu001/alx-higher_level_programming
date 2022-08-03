#!/usr/bin/python3
"""Module containing interview function

"""


def pascal_triangle(n):
    """ Returns a list according to pascal's triangle

    """
    lists = []

    if n <= 0:
        return lists
    
    for idx in range(1, n + 1):
        tmp = []
        for i in range(idx):
            if i == 0 or i == idx - 1:
                tmp.append(1)
            else:
                tmp.append(lists[idx - 2][i - 1] + lists[idx - 2][i])
        lists.append(tmp)
    return lists
