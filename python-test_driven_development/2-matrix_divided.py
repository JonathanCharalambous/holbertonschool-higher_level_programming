#!/usr/bin/python3
"""
This module provides the matrix_divided function that 
divides a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
   Divides each number on a matrix by the provided number.

    Args:
        a: The maxtrix.
        b: The number to divide by.

    Returns:
        The divided matrix.

    Raises:
        TypeError: If div is not an integer or float.
        TypeError: If each row of the matrix is not the same size.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or \
        any(not isinstance(row, list) for \
            row in matrix) or \
        any(not isinstance(item, (int, float)) for \
            row in matrix for item in row):
            raise TypeError("matrix must be a matrix \
            (list of lists) of integers/floats")
    for row in matrix:
         if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round((num / div), 2) for num in row] for row in matrix]
