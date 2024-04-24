#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize first row

    for _ in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # First element of each row is always 1

        # Calculate middle elements of the row
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])

        new_row.append(1)  # Last element of each row is always 1
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle

# Test the function


def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


print_triangle(pascal_triangle(5))
