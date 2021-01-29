"""
Problem:

A tree is symmetric if its data and shape remain unchanged when it is reflected about
the root node. The following tree is an example:

        4
      / | \
    3   5   3
  /           \
9              9
Given a k-ary tree, determine whether it is symmetric.
"""

from typing import Dict, List


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.children = []

    def __str__(self) -> str:
        return "{} -> {}".format(self.val, self.children)


def generate_tree_levels(
    root: Node, levels: Dict[int, List[int]], level_number: int
) -> Dict[int, List[int]]:
    # DFS to generate the nodes in the tree by level
    if level_number not in levels:
        levels[level_number] = []
    levels[level_number].append(root.val)
    for child in root.children:
        generate_tree_levels(child, levels, level_number + 1)
    return levels


def is_symmetric(node: Node) -> bool:
    levels = generate_tree_levels(node, {}, 0)
    # checking if the tree is symmetric
    for level_values in levels.values():
        if level_values != level_values[::-1]:
            return False
    return True


if __name__ == "__main__":
    a = Node(4)
    b = Node(5)
    c = Node(3)
    d = Node(3)
    e = Node(9)
    f = Node(9)

    a.children = [c, b, d]

    c.children = [f]
    d.children = [e]

    print(is_symmetric(a))

    c.children = [f, Node(1)]
    d.children = [Node(1), e]

    print(is_symmetric(a))

    c.val = 4
    print(is_symmetric(a))


"""
SPECS:

TIME COMPLEXITY: O(n + e)
SPACE COMPLEXITY: O(n)
"""
