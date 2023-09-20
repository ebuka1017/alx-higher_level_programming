#!/usr/bin/python3
"""func to divide a matrix"""


def matrix_divided(matrix, div):
    """
    divide a matrix (list of lists)
    """
    for row in matrix:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    nm = [[round(x / div, 2) for x in row] for row in matrix]

    return nm
