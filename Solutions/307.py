"""
Problem:

Given a binary search tree, find the floor and ceiling of a given integer. The floor is
the highest element in the tree less than or equal to an integer, while the ceiling is
the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.
"""

from typing import Optional, Tuple

from DataStructures.Tree import BinarySearchTree, Node


def get_ceiling(node: Node, value: int) -> Optional[int]:
    # function to get the ceiling of the input in a binary search tree
    # using BST property to find the element optiomally
    if node.val > value:
        if node.left:
            if node.left.val >= value:
                return get_ceiling(node.left, value)
            return node.val
        return node.val
    elif node.val == value:
        return value
    else:
        if node.right:
            return get_ceiling(node.right, value)
        return None


def get_floor(node: Node, value: int) -> Optional[int]:
    # function to get the floor of the input in a binary search tree
    # using BST property to find the element optiomally
    if node.val < value:
        if node.right:
            if node.right.val <= value:
                return get_floor(node.right, value)
            return node.val
        return node.val
    elif node.val == value:
        return value
    else:
        if node.left:
            return get_floor(node.left, value)
        return None


def get_floor_and_ceiling(
    tree: BinarySearchTree, value: int
) -> Tuple[Optional[int], Optional[int]]:
    # function to get the ceiling and floor of the input in a binary search tree
    if tree.root:
        return get_floor(tree.root, value), get_ceiling(tree.root, value)
    return None, None


if __name__ == "__main__":
    tree = BinarySearchTree()

    tree.add(4)
    tree.add(2)
    tree.add(1)
    tree.add(3)
    tree.add(6)

    print(get_floor_and_ceiling(tree, 2))
    print(get_floor_and_ceiling(tree, 7))
    print(get_floor_and_ceiling(tree, -1))
    print(get_floor_and_ceiling(tree, 5))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(log(n))
"""
