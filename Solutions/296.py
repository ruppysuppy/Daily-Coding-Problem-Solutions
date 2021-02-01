"""
Problem:

Given a sorted array, convert it into a height-balanced binary search tree.
"""

from typing import List

from DataStructures.Tree import BinarySearchTree


def create_balanced_bst_helper(arr: List[int], tree: BinarySearchTree) -> None:
    # based on the fact that a sorted array middle element has approximately (with at
    # most difference of 1) equal number of elements on its either side
    if len(arr) == 0:
        return
    mid = len(arr) // 2
    tree.add(arr[mid])
    create_balanced_bst_helper(arr[:mid], tree)
    create_balanced_bst_helper(arr[mid + 1 :], tree)


def create_balanced_bst(arr: List[int]) -> BinarySearchTree:
    tree = BinarySearchTree()
    create_balanced_bst_helper(arr, tree)
    return tree


if __name__ == "__main__":
    print(create_balanced_bst([1, 2, 3, 4, 5]))
    print(create_balanced_bst([1, 2, 3, 4, 5, 6, 7]))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(n)
[time complexity can be reduced to O(n) using node reference inplace of calling
tree.add()]
"""
