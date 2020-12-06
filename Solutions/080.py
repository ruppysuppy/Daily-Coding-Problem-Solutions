"""
Problem:

Given the root of a binary tree, return a deepest node. For example, in the following
tree, return d.

    a
   / \
  b   c
 /
d
"""

from typing import Optional, Tuple

from DataStructures.Tree import BinaryTree, Node


def deepest_node_helper(node: Node) -> Tuple[int, Optional[Node]]:
    if node is None:
        return 0, None
    if not (node.left and node.right):
        return 1, node
    # getting the deepest node of the left-subtree
    left_height, left_node = 0, None
    if node.left:
        left_height, left_node = deepest_node_helper(node.left)
    # getting the deepest node of the right-subtree
    right_height, right_node = 0, None
    if node.right:
        right_height, right_node = deepest_node_helper(node.right)
    # comparing and returning the deepest node
    if left_height > right_height:
        return left_height + 1, left_node
    return right_height + 1, right_node


def deepest_node(tree: BinaryTree) -> Node:
    _, node = deepest_node_helper(tree.root)
    return node


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node("a")

    tree.root.left = Node("b")
    tree.root.right = Node("c")

    tree.root.left.left = Node("d")

    print(deepest_node(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n)) [recursion depth]
"""
