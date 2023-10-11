#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    """
        Args:
            matrix: array of integers

        Returns:
            new_matrix
    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            square_value = col ** 2
            new_row.append(square_value)
        new_matrix.append(new_row)

    return new_matrix
