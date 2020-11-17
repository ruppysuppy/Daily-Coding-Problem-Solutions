"""
Problem:

Given the root to a binary search tree, find the second largest node in the tree.
"""

from typing import Optional, Tuple

from DataStructures.Tree import Node, BinarySearchTree


def get_largest_pair_from_current_node(node: Node) -> Tuple[Optional[Node], Node]:
    parent = None
    while node.right:
        parent = node
        node = node.right
    # both the parent and the node is returned
    return parent, node


def get_second_largest(tree: BinarySearchTree) -> Optional[int]:
    if tree.root is None:
        return None

    parent_of_largest, largest = get_largest_pair_from_current_node(tree.root)
    # if the largest node has a left node, the largest child of the left node is the
    # 2nd largest node (BST property)
    if largest.left:
        _, second_largest_node = get_largest_pair_from_current_node(largest.left)
        return second_largest_node.val
    # if the left node and the parent is absent (the tree contains only 1 node),
    # None is returned
    elif parent_of_largest is None:
        return None
    # if the largest parent is present its the 2nd largest node if no left node is
    # present (BST property)
    return parent_of_largest.val


if __name__ == "__main__":
    tree = BinarySearchTree()

    tree.add(5)
    tree.add(3)
    tree.add(8)
    tree.add(2)
    tree.add(4)
    tree.add(7)
    tree.add(9)

    print(get_second_largest(tree))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(1)
"""
