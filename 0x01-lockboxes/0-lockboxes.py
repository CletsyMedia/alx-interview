#!/usr/bin/python3
"""Determines if all boxes can be opened from a list of lists."""


def canUnlockAll(boxes=[]):
    """Determines if all boxes can be opened.

    Args:
        boxes (list of list): A list of lists representing the boxes and
        their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    keys = set([0])
    for box_id, box in enumerate(boxes):
        for key in box:
            if key < len(boxes) and key != box_id:
                keys.add(key)

    if len(keys) != len(boxes):
        return False

    return True


if __name__ == '__main__':
    boxes = [
        [1, 3],
        [2],
        [3, 0],
        [1, 2, 3],
    ]
    print(canUnlockAll(boxes))

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
