"""
Problem:

In Ancient Greece, it was common to write text with the first line going left to right,
the second line going right to left, and continuing to go back and forth. This style
was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].
"""

from typing import Dict, List
from DataStructures.Tree import Node, BinaryTree


def get_boustrophedon_helper(
    node: Node, level: int, accumulator: Dict[int, List[int]]
) -> None:
    # using dfs to store a list of values by level
    if level not in accumulator:
        accumulator[level] = []
    accumulator[level].append(node.val)
    if node.left:
        get_boustrophedon_helper(node.left, level + 1, accumulator)
    if node.right:
        get_boustrophedon_helper(node.right, level + 1, accumulator)


def get_boustrophedon(tree: BinaryTree) -> List[int]:
    if not tree.root:
        return []
    # generating the nodes by level
    level_data = {}
    get_boustrophedon_helper(tree.root, 1, level_data)
    result = []
    # adding the even levels in reverse order in the result
    for level in sorted(list(level_data.keys())):
        if level % 2 == 0:
            result.extend(reversed(level_data[level]))
        else:
            result.extend(level_data[level])
    return result


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)

    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print(get_boustrophedon(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
