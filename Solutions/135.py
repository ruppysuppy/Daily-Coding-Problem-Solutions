"""
Problem:

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

from typing import List, Tuple

from DataStructures.Tree import BinaryTree, Node


def minimum_path_sum_helper(node: Node) -> Tuple[int, List[int]]:
    left_sum, left = None, None
    right_sum, right = None, None
    if node.left:
        left_sum, left = minimum_path_sum_helper(node.left)
    if node.right:
        right_sum, right = minimum_path_sum_helper(node.right)
    # generating the minimum path sum
    if not left and not right:
        return node.val, [node.val]
    elif left and not right:
        return (left_sum + node.val), left + [node.val]
    elif right and not left:
        return (right_sum + node.val), right + [node.val]
    return min(
        ((left_sum + node.val), left + [node.val]),
        ((right_sum + node.val), right + [node.val]),
        key=lambda x: x[0],
    )


def minimum_path_sum(tree: BinaryTree) -> List[int]:
    if not tree.root:
        raise ValueError("Empty Tree")
    _, path = minimum_path_sum_helper(tree.root)
    return path[::-1]


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(10)

    tree.root.left = Node(5)
    tree.root.right = Node(5)

    tree.root.left.right = Node(2)

    tree.root.right.right = Node(1)

    tree.root.right.right.left = Node(-1)

    print(tree)
    print(minimum_path_sum(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
