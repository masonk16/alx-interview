#!/usr/bin/python3
"""
Island Perimeter Coding Challenge.
"""


def island_perimeter(grid):
    """
    :grid:  list of list of integers
    :returns: perimeter of the island described in grid
    """
    island = 0  # 0
    neighbor = 0  # 3

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                island = island + 1
                if x < len(grid[y]) - 1 and grid[y][x + 1] == 1:
                    neighbor = neighbor + 1
                if y < len(grid) - 1 and grid[y + 1][x] == 1:
                    neighbor = neighbor + 1
    return island * 4 - 2 * neighbor
