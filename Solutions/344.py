"""
Problem:

You are given a tree with an even number of nodes. Consider each connection between a
parent and child node to be an "edge". You would like to remove some of these edges,
such that the disconnected subtrees that remain each have an even number of nodes.

For example, suppose your input was the following tree:

   1
  / \ 
 2   3
    / \ 
   4   5
 / | \
6  7  8

In this case, removing the edge (3, 4) satisfies our requirement.

Write a function that returns the maximum number of edges you can remove while still
satisfying this requirement.
"""

from __future__ import annotations
from typing import List, Tuple


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.children = []

    def add_children(self, children: List[Node] = []) -> None:
        self.children = [*children]


class Tree:
    def __init__(self) -> None:
        self.root = None


def get_even_edge_split_helper(node: Node) -> Tuple[int, int]:
    nodes_count = 0
    even_splits = 0
    for child in node.children:
        child_nodes, child_even_splits = get_even_edge_split_helper(child)
        nodes_count += child_nodes
        even_splits += child_even_splits
        if child_nodes != 0 and child_nodes % 2 == 0:
            even_splits += 1
    return nodes_count + 1, even_splits


def get_even_edge_split(tree: Tree) -> int:
    if tree.root:
        _, result = get_even_edge_split_helper(tree.root)
        return result
    return 0


if __name__ == "__main__":
    tree = Tree()

    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(8)

    a.add_children([b, c])
    c.add_children([d, e])
    d.add_children([f, g, h])

    tree.root = a

    print(get_even_edge_split(tree))  # possible splits at (1, 3) and (3, 4)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
