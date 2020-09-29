#!/usr/bin/python3
"""
function that divides a matrix of ints
"""


def matrix_divided(matrix, div):
    """
    divides the matrixes
    """

    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) of integers\floats')

    matrix_length = len(matrix[0])
    for i in matrix:
        if len(i) != matrix_length:
            raise TypeError('Each row of the matrix must be the same size')
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of\
                             integers/floats')

    if not isinstance(j, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    final_matrix = []
    for i in matrix:
        new_matrix = []
        for j in i:
            new_matrix.append(round(j / div, 2))
        final_matrix.append(new_matrix)

    return final_matrix
