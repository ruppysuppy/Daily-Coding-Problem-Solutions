"""
Problem:

The horizontal distance of a binary tree node describes how far left or right the node
will be when the tree is printed out.

More rigorously, we can define it as follows:

The horizontal distance of the root is 0.
The horizontal distance of a left child is hd(parent) - 1.
The horizontal distance of a right child is hd(parent) + 1.
For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
The bottom view of a tree, then, consists of the lowest node at each horizontal
distance. If there are two nodes at the same depth and horizontal distance, either is
acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.
"""

from typing import Dict, List, Tuple

from DataStructures.Tree import Node, BinaryTree


def get_bottom_view_helper(
    node: Node, depth: int, hd: int, accumulator: Dict[int, Tuple[int, int]]
) -> Dict[int, Tuple[int, int]]:
    if hd not in accumulator:
        accumulator[hd] = (depth, node.val)
    elif accumulator[hd][0] <= depth:
        accumulator[hd] = (depth, node.val)

    if node.left:
        get_bottom_view_helper(node.left, depth + 1, hd - 1, accumulator)
    if node.right:
        get_bottom_view_helper(node.right, depth + 1, hd + 1, accumulator)
    return accumulator


def get_bottom_view(tree: BinaryTree) -> List[int]:
    data = get_bottom_view_helper(tree.root, 0, 0, {})
    res_arr = [(hd, data[hd][1]) for hd in data]
    res_arr.sort(key=lambda elem: elem[0])
    return [elem for _, elem in res_arr]


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(5)

    tree.root.left = Node(3)
    tree.root.right = Node(7)

    tree.root.left.left = Node(1)
    tree.root.left.right = Node(4)

    tree.root.right.left = Node(6)
    tree.root.right.right = Node(9)

    tree.root.left.left.left = Node(0)

    tree.root.right.right.left = Node(8)

    print(tree)
    print(get_bottom_view(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
