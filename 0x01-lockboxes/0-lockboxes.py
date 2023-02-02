#!/usr/bin/python3
"""
Lockboxes Coding Challenge
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    param boxes: a list of lists containing integers.
    return: True if all boxes can be opened, else return False.
    """

    opened_boxes = [0]

    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in opened_boxes and key != box_id:
                opened_boxes.append(key)

    if len(opened_boxes) == len(boxes):
        return True
    return False
