#!/usr/bin/python3
"""
module that implements the class Pascal's triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of ints representing Pascal's triangle of n
    """

    if n <= 0:
        return ""

    first = [[1]]
    for next_row in range(1, n):
        row = [1]
        prev = first[next_row - 1]
        for pos in range(1, next_row):
            row.append(prev[pos] + prev[pos - 1])
        row.append(1)
        first.append(row)
    return first
