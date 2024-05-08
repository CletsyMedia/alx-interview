#!/usr/bin/python3

"""Minimum Operations: Given a number n, calculate the fewest number of
operations needed to result in exactly n H characters in a text file."""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed.

    Raises:
        TypeError: If n is not an integer.

    Notes:
        If n is impossible to achieve, returns 0.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    operations = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
