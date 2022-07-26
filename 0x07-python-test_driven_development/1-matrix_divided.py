#!/usr/bin/python3
"""A module containing function that divides a matrix.

>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

"""


def matrix_divided(matrix, div):
    """A function that divides a matrix

    Args:
        matrix (:ob:`list` of :ob:`list` of int): Matrix to be divided.
        div (int): Number used to divide.

    Raises:
        TypeError: if div is not a number.
        ZeroDivisionError: if div is zero.
        TypeError: if the the rows of the matrix are not the same size.
        TypeError: if not a matrix of ints and floats.

    Returns:
        :obj:`list` of :obj:`list` of int: The new matrix.

    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

        std_len = len(matrix[0])
        if len(row) != std_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for column in row:
            if type(column) is not int and type(column) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            new_column = round(column / div, 2)
            new_row.append(new_column)
        new_matrix.append(new_row)
    return new_matrix
