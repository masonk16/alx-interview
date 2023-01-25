#!/usr/bin/python3
"""Pascal's Triangle Coding Challenge"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    
    a = []

    for i in range(n):
        a.append([])
        a[i].append(1)
        for j in range (1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])

    return a
