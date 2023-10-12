#!/usr/bin/python3
# 101-square_matrix_map.py

def square_matrix_map(matrix=[]):
    """ square matrix function

        Args:
            matrix: input

        Returns:
            new_matrix
    """
    return list(map(lambda col: list(map(lambda x: x**2, col)), matrix))
