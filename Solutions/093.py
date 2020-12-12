"""
Problem:

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
"""

from sys import maxsize
from typing import Tuple

from DataStructures.Tree import BinaryTree, Node


def get_largest_bst_size_helper(node: Node) -> Tuple[int, Node, bool, int, int]:
    if not node:
        return 0, node, True, maxsize, -maxsize
    if not node.left and not node.right:
        return 1, node, True, node.val, node.val

    l_height, l_root, l_is_bst, l_max_val, l_min_val = get_largest_bst_size_helper(
        node.left
    )
    r_height, r_root, r_is_bst, r_max_val, r_min_val = get_largest_bst_size_helper(
        node.right
    )
    if l_is_bst and r_is_bst:
        if node.left and node.right:
            if l_max_val <= node.val <= r_min_val:
                return (l_height + r_height + 1), node, True, r_max_val, l_min_val
        else:
            if node.left and node.val > l_max_val:
                return l_height + 1, node, True, node.val, l_min_val
            elif node.right and node.val < r_min_val:
                return r_height + 1, node, True, r_max_val, node.val
    if l_height > r_height:
        return l_height, l_root, False, l_max_val, l_min_val
    return r_height, r_root, False, r_max_val, r_min_val


def get_largest_bst_size(tree: BinaryTree) -> Tuple[int, int]:
    size, node, _, _, _ = get_largest_bst_size_helper(tree.root)
    return size, node.val


if __name__ == "__main__":
    a = Node(3)
    b = Node(2)
    c = Node(6)
    d = Node(1)
    e = Node(1)
    f = Node(4)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    tree = BinaryTree()
    tree.root = a

    print(tree)
    print("Size: {}\tNode Val: {}".format(*get_largest_bst_size(tree)))

    a = Node(3)
    b = Node(2)
    c = Node(6)
    d = Node(1)
    e = Node(4)
    f = Node(4)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    tree = BinaryTree()
    tree.root = a

    print(tree)
    print("Size: {}\tNode Val: {}".format(*get_largest_bst_size(tree)))

    a = Node(1)
    b = Node(2)
    c = Node(6)
    d = Node(1)
    e = Node(3)
    f = Node(4)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    tree = BinaryTree()
    tree.root = a

    print(tree)
    print("Size: {}\tNode Val: {}".format(*get_largest_bst_size(tree)))

    a = Node(3)
    b = Node(2)
    c = Node(6)
    d = Node(1)
    e = Node(3)
    f = Node(4)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    tree = BinaryTree()
    tree.root = a

    print(tree)
    print("Size: {}\tNode Val: {}".format(*get_largest_bst_size(tree)))

    a = Node(3)
    b = Node(1)
    c = Node(6)
    d = Node(0)
    e = Node(2)
    f = Node(4)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    tree = BinaryTree()
    tree.root = a

    print(tree)
    print("Size: {}\tNode Val: {}".format(*get_largest_bst_size(tree)))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n))
"""
