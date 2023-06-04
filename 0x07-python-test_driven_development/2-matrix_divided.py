#!/usr/bin/python3

"""
A function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix: a list of lists of ints/floats
        div: divisor that's also int/float

    Raises:
        TypeError: If matrix contains non numbers
        TypeError: If matrix contains rows that aren't of equal size
        TypeError: If div isn't an int or float
        ZeroDivisonError: If div is 0

    Returns:
        A new matrix representing the result of the division
    """

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if (not isinstance(matrix, list) or matrix == [] or
                    not all(isinstance(row, list) for row in matrix) or
                    not isinstance(matrix[r][c], (float, int))):
                raise TypeError("matrix must be a "
                                "matrix (list of lists) of integers/floats"
                                )
    len_row_1 = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != len_row_1:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
