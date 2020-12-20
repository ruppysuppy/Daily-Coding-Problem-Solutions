"""
Problem:

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the
tree. Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined
between two nodes v and w as the lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself)."
"""

from __future__ import annotations
from typing import Optional

from DataStructures.Tree import BinaryTree


class Node:
    def __init__(self, val: int, parent: Optional[Node] = None) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent

    def __eq__(self, other: Node) -> bool:
        return self is other

    def __hash__(self) -> int:
        return hash(self.val)

    def __repr__(self) -> str:
        return self.str_representation()

    def str_representation(self) -> str:
        if self.right is None and self.left is None:
            return f"('{self.val}')"
        elif self.left is not None and self.right is None:
            return f"({self.left.str_representation()}, '{self.val}', None)"
        elif self.left is not None and self.right is not None:
            return (
                f"({self.left.str_representation()},"
                + f" '{self.val}', {self.right.str_representation()})"
            )
        elif self.left is None and self.right is not None:
            return f"(None, '{self.val}', {self.right.str_representation()})"


def get_lca(node1: Node, node2: Node) -> Optional[Node]:
    node1_ancestors = set()
    node = node1
    while node:
        node1_ancestors.add(node)
        node = node.parent
    node = node2
    while node:
        if node in node1_ancestors:
            return node
        node = node.parent
    return None


if __name__ == "__main__":
    tree = BinaryTree()

    a = Node(1)
    b = Node(2, parent=a)
    c = Node(3, parent=a)
    d = Node(4, parent=b)
    e = Node(5, parent=b)
    f = Node(6, parent=c)
    g = Node(7, parent=c)

    tree.root = a

    tree.root.left = b
    tree.root.right = c

    tree.root.left.left = d
    tree.root.left.right = e

    tree.root.right.left = f
    tree.root.right.right = g

    print(tree)

    print(get_lca(f, g))
    print(get_lca(a, g))
    print(get_lca(d, g))
    print(get_lca(a, c))
    print(get_lca(e, b))
    print(get_lca(a, Node(8)))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(log(n))
"""
