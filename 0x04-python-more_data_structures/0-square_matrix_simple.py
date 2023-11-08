#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    new_matrix = []
    for row in matrix:
        # new_matrix.append([x ** 2 for x in row])
        # new_matrix.append(list(map(lambda x: x * x, row)))
        # new_matrix.append(list(map(lambda x: pow(x, 2), row)))
        # all of the above are valid
        new_matrix.append(list(map(lambda x: x ** 2, row)))
    return new_matrix
