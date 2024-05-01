#!/usr/bin/python3
"""
Determines if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list): A list of lists representing the boxes and
        their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()

    # Initialize a stack with the first box
    stack = [0]

    # Iterate over the stack until it's empty
    while stack:
        # Pop the last element from the stack
        current_box = stack.pop()

        # If the current box has not been visited yet
        if current_box not in visited:
            # Add it to the visited set
            visited.add(current_box)

            # Add all keys from the current box to the stack
            for key in boxes[current_box]:
                stack.append(key)

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
