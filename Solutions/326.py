"""
Problem:

A Cartesian tree with sequence S is a binary tree defined by the following two
properties:

It is heap-ordered, so that each parent value is strictly less than that of its
children. An in-order traversal of the tree produces nodes with values that correspond
exactly to S. For example, given the sequence [3, 2, 6, 1, 9], the resulting Cartesian
tree would be:

      1
    /   \   
  2       9
 / \
3   6
Given a sequence S, construct the corresponding Cartesian tree.
"""

from typing import List, Optional

from DataStructures.Tree import Node, BinaryTree


def generate_cartesian_tree_helper(
    arr: List[int], last: Optional[Node] = None, root: Optional[Node] = None
) -> Node:
    if not arr:
        return root
    # Cartesian tree generation
    node = Node(arr[0])
    if not last:
        # root of the tree
        return generate_cartesian_tree_helper(arr[1:], node, node)
    if last.val > node.val:
        # property of Cartesian tree
        node.left = last
        return generate_cartesian_tree_helper(arr[1:], node, node)
    last.right = node
    return generate_cartesian_tree_helper(arr[1:], last, last)


def generate_cartesian_tree(sequence: List[int]) -> BinaryTree:
    tree = BinaryTree()
    tree.root = generate_cartesian_tree_helper(sequence)
    return tree


if __name__ == "__main__":
    print(generate_cartesian_tree([3, 2, 6, 1, 9]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
