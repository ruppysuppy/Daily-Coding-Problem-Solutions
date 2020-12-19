"""
Problem:

Given a binary tree, return all paths from the root to leaves.

For example, given the tree

   1
  / \
 2   3
    / \
   4   5
it should return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""

from typing import List

from DataStructures.Tree import BinaryTree, Node


def get_paths_helper(node: Node, paths: List[int], curr_path: List[int]) -> None:
    if not node.left and not node.right:
        # leaf node
        curr_path.append(node.val)
        paths.append([*curr_path])
        curr_path.pop()
        return
    # non-leaf node
    curr_path.append(node.val)
    if node.left:
        get_paths_helper(node.left, paths, curr_path)
    if node.right:
        get_paths_helper(node.right, paths, curr_path)
    curr_path.pop()


def get_paths(tree: BinaryTree):
    if not tree.root:
        return []
    paths = []
    get_paths_helper(tree.root, paths, [])
    return paths


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)

    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)

    print(tree)
    print(get_paths(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n))
"""
