#!/usr/bin/python3

"""

This module includes a function for matrix multiplication of two metrics.

"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
        or contains non-numeric elements.
        ValueError: If m_a or m_b is empty, not rectangular,
        or cannot be multiplied.
    """

    # validate m_a and m_b matrices

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(sublist, list) for sublist in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(sublist, list) for sublist in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if (not all(isinstance(element, (int, float))
                for row in m_a for element in row)):
        raise TypeError("m_a should contain only integers or floats")
    if (not all(isinstance(element, (int, float))
                for row in m_b for element in row)):
        raise TypeError("m_b should contain only integers or floats")

    row_a = len(m_a[0])
    if not all(len(row) == row_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_b = len(m_b[0])
    if not all(len(row) == row_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate if m_b and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication

    result = []

    for row_a in m_a:
        current_row = []
        for col_b in zip(*m_b):
            current_row.append(sum(a * b for a, b in zip(row_a, col_b)))
        result.append(current_row)

    return result
