#!/usr/bin/python3
"""Pascal's Triangle Coding Challenge"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle_list = [0] * n

    for i in range(n):
        new_list = [0] * (i + 1)
        new_list[0] = 1
        new_list[len(new_list) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(new_list):
                a = triangle_list[i - 1][j]
                b = triangle_list[i - 1][j - 1]
                new_list[j] = a + b

        triangle_list[i] = new_list

    return triangle_list
