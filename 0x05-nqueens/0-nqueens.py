#!/usr/bin/python3
"""
N Queens Coding Challenge
"""

import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

# NxN matrix with all elements 0
board = [[0] * N for _ in range(N)]


def is_attack(i, j):
    """
    Checking if there is a queen in row or column
    """
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # checking diagonals
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False


def N_queen(n):
    """
    Checking if we can place a queen here or not
    queen will not be placed if the place is being
    attacked    or already occupied.
    """
    for i in range(0, N):
        for j in range(0, N):

            if (not (is_attack(i, j))) and (board[i][j] != 1):
                board[i][j] = 1

                if N_queen(n - 1) == True:
                    return True
                board[i][j] = 0

    return False


N_queen(N)
for i in board:
    print(i)

