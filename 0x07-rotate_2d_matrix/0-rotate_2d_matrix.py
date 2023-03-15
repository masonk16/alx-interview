#!/usr/bin/python3
"""
Rotate 2D Matrix Coding Challenge.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate it 90 degrees clockwise.
    :param matrix: non-empty, n x n 2D matrix.
    :return:
    """
    # list(zip(*matrix[::-1]))

    temp_matrix = []

    column = len(matrix) - 1

    for column in range(len(matrix)):
        temp = []
        for row in range(len(matrix) - 1, -1, -1):
            temp.append(matrix[row][column])
        temp_matrix.append(temp)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = temp_matrix[i][j]
