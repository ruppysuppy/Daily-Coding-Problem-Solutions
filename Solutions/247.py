"""
Problem:

Given a binary tree, determine whether or not it is height-balanced. A height-balanced
binary tree can be defined as one in which the heights of the two subtrees of any node
never differ by more than one.
"""

from typing import Tuple

from DataStructures.Tree import Node, BinaryTree


def height_helper(node: Node) -> Tuple[int, bool]:
    if node.left is None:
        left_height, balance_left = 0, True
    else:
        left_height, balance_left = height_helper(node.left)
    if node.right is None:
        right_height, balance_right = 0, True
    else:
        right_height, balance_right = height_helper(node.right)

    balance = balance_left and balance_right
    current_balance = -1 <= (right_height - left_height) <= 1
    height = max(left_height, right_height) + 1
    return height, balance and current_balance


def check_balance(tree: BinaryTree) -> bool:
    if tree.root is None:
        return True
    _, balance = height_helper(tree.root)
    return balance


if __name__ == "__main__":
    tree = BinaryTree()

    tree.root = Node(0)

    tree.root.left = Node(1)
    tree.root.right = Node(2)

    tree.root.left.left = Node(3)
    tree.root.left.right = Node(4)

    print(check_balance(tree))

    tree.root.left.right.left = Node(5)

    print(check_balance(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n))
"""
