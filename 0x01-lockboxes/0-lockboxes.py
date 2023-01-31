#!/usr/bin/python3
"""Lockboxes Coding Challenge"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    param boxes: a list of lists containing integers.
    return: True if all boxes can be opened, else return False.
    """
    unlocked_boxes = [0]
    for box_index, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked_boxes and key != box_index:
                unlocked_boxes.append(key)
    if len(unlocked_boxes) == len(boxes):
        return True
    return False
