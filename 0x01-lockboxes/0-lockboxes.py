#!/usr/bin/python3
'''LockBoxes Challenge'''

def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Args:
        boxes (list): List of lists where each sublist represents keys in a box
    Returns:
        bool: True if all boxes can be opened, False otherwise
    '''
    length = len(boxes)
    keys = set(boxes[0])  # Start with the keys in the first box
    opened_boxes = set([0])  # First box is always opened

    while keys:
        key = keys.pop()
        if key < length and key not in opened_boxes:
            opened_boxes.add(key)
            keys.update(boxes[key])  # Add new keys found in the newly opened box

    # Check if all boxes are opened
    return len(opened_boxes) == length

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False

