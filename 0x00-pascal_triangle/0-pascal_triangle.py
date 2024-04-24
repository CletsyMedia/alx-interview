#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n."""
    if n <= 0:
        return []

    pascal = [[] for idx in range(n)]

    for li in range(n):
        for col in range(li + 1):
            if col < li:
                if col == 0:
                    pascal[li].append(1)
                else:
                    pascal[li].append(pascal[li - 1][col] +
                                      pascal[li - 1][col - 1])
            elif col == li:
                pascal[li].append(1)

    return pascal
