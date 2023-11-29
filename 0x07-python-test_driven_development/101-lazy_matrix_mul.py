#!/usr/bin/python3

"""
Module to multiply two matrices using the module NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices using the module NumPy

    args:
        m_a (list): first matrix
        m_b (list): second matrix

    returns:
        the result of the multiplication
    """
    return np.matmul(m_a, m_b)
