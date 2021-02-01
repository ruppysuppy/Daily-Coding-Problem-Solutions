"""
Problem:

Two nodes in a binary tree can be called cousins if they are on the same level of the
tree but have different parents. For example, in the following diagram 4 and 6 are
cousins.

    1
   / \
  2   3
 / \   \
4   5   6
Given a binary tree and a particular node, find all cousins of that node.
"""

from typing import List, Optional

from DataStructures.Tree import BinaryTree, Node


def get_depth_dfs_helper(
    node: Node, search_node_val: int, depth: int, parent_val: Optional[int] = None
) -> Optional[int]:
    if node.val == search_node_val:
        return depth, parent_val
    if node.left:
        left_depth, parent = get_depth_dfs_helper(
            node.left, search_node_val, depth + 1, node
        )
        if left_depth:
            return left_depth, parent
    if node.right:
        right_depth, parent = get_depth_dfs_helper(
            node.right, search_node_val, depth + 1, node
        )
        if right_depth:
            return right_depth, parent
    return None, None


def get_node_by_depth(
    node: Node,
    curr_depth: int,
    depth: int,
    search_node_val: int,
    accumulator: int,
    ignore_parent_val: int,
    parent_val: Optional[int] = None,
) -> None:
    # getting all nodes where the depth is equal to the input depth (except the node
    # with black-listed parent ["ignore_parent_val"])
    if parent_val == ignore_parent_val:
        return
    if node.val == search_node_val:
        return
    if curr_depth == depth:
        accumulator.append(node.val)
        return
    if node.left:
        get_node_by_depth(
            node.left,
            curr_depth + 1,
            depth,
            search_node_val,
            accumulator,
            ignore_parent_val,
            node,
        )
    if node.right:
        get_node_by_depth(
            node.right,
            curr_depth + 1,
            depth,
            search_node_val,
            accumulator,
            ignore_parent_val,
            node,
        )


def dfs_get_depth(tree: BinaryTree, search_node_val: int):
    return get_depth_dfs_helper(tree.root, search_node_val, 0)


def get_cousins(tree: BinaryTree, node_val: int) -> List[int]:
    depth, parent = dfs_get_depth(tree, node_val)
    if depth is None:
        raise ValueError("Node not present in Tree")
    cousins = []
    get_node_by_depth(tree.root, 0, depth, node_val, cousins, parent)
    return cousins


if __name__ == "__main__":
    tree = BinaryTree()

    tree.root = Node(1)

    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    tree.root.right.right = Node(6)

    print(tree)
    print(get_cousins(tree, 4))

    tree.root.right.left = Node(7)

    print(tree)
    print(get_cousins(tree, 4))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
