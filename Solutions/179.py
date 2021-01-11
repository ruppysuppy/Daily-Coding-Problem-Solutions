"""
Problem:

Given the sequence of keys visited by a postorder traversal of a binary search tree,
reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following
tree:

    5
   / \
  3   7
 / \   \
2   4   8
"""

from typing import List

from DataStructures.Tree import BinarySearchTree, Node


def bst_from_postorder(postorder: List[int]) -> BinarySearchTree:
    tree = BinarySearchTree()
    if postorder:
        tree.add(postorder[-1])
        for val in postorder[-2::-1]:
            tree.add(val)
    return tree


if __name__ == "__main__":
    print(bst_from_postorder([2, 4, 3, 8, 7, 5]))


"""
SPECS:

TIME COMPLEXITY: O(n log(n))
SPACE COMPLEXITY: O(n)
"""
