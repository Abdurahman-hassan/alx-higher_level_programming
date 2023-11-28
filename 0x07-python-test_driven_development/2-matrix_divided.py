#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with all elements divided by div.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   if rows of the matrix are not the same size,
                   or if div is not an integer or a float.
        ZeroDivisionError: If div is zero.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if ((not isinstance(matrix, list) or not matrix) or
            (not all(isinstance(sublist, list) and sublist and
                     all(isinstance(element,
                                    (int, float)) for element in sublist)
                     for sublist in matrix))):
        raise TypeError(error_msg)

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
