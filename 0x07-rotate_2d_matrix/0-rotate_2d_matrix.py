#!/usr/bin/env python3
"""
Rotate 2D Matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate it 90 degrees clockwise.
    :param matrix: non-empty, n x n 2D matrix.
    :return:
    """
    # Construct an output matrix with the correct dimensions, i.e.
    # # of rows and columns are switched.
    output = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    # Reverse the matrix, row-wise.
    for i in range(int(len(matrix) / 2)):
        matrix[i], matrix[len(matrix)-1-i] = matrix[len(matrix)-1-i], matrix[i]

    # Switch the x and y coordinates.
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            output[j][i] = matrix[i][j]

    print(output)
