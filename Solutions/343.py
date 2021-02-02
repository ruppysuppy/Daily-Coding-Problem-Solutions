"""
Problem:

Given a binary search tree and a range [a, b] (inclusive), return the sum of the
elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).
"""

from typing import Tuple

from DataStructures.Tree import BinarySearchTree, Node


def get_sum_over_range_helper(node: Node, low: int, high: int) -> int:
    if node is None:
        return 0
    if low <= node.val <= high:
        return (
            node.val
            + get_sum_over_range_helper(node.left, low, high)
            + get_sum_over_range_helper(node.right, low, high)
        )
    elif low > node.val:
        return get_sum_over_range_helper(node.right, low, high)
    return get_sum_over_range_helper(node.left, low, high)


def get_sum_over_range(tree: BinarySearchTree, sum_range: Tuple[int, int]) -> int:
    if tree.root is None:
        return 0
    low, high = sum_range
    return get_sum_over_range_helper(tree.root, low, high)


if __name__ == "__main__":
    tree = BinarySearchTree()

    tree.add(5)
    tree.add(3)
    tree.add(8)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(10)

    print(get_sum_over_range(tree, (4, 9)))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(height_of_the_tree) [due to recursion]
"""
