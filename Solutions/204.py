"""
Problem:

Given a complete binary tree, count the number of nodes in faster than O(n) time.
Recall that a complete binary tree has every level filled except the last, and the
nodes in the last level are filled starting from the left.
"""

from typing import Optional

from DataStructures.Tree import BinaryTree, Node


def get_num_node_complete_bin_tree_helper(
    node: Node,
    left_route_levels: Optional[int] = None,
    right_route_levels: Optional[int] = None,
) -> int:
    # generating the route levels incase it is not passed to the function
    if left_route_levels is None:
        curr_node = node
        while curr_node:
            curr_node = curr_node.left
            left_route_levels += 1
    if right_route_levels is None:
        curr_node = node
        while curr_node:
            curr_node = curr_node.right
            right_route_levels += 1
    # checking if the binary tree is completely filled
    if left_route_levels == right_route_levels:
        return pow(2, left_route_levels) - 1
    # getting the number of nodes in the sub-trees
    left_route_nodes, right_route_nodes = 0, 0
    if node.left:
        left_route_nodes = get_num_node_complete_bin_tree_helper(
            node.left, left_route_levels - 1, 0
        )
    if node.right:
        right_route_nodes = get_num_node_complete_bin_tree_helper(
            node.right, 0, right_route_levels - 1
        )
    return left_route_nodes + right_route_nodes + 1


def get_num_node_complete_bin_tree(tree: BinaryTree) -> int:
    if not tree.root:
        return 0
    return get_num_node_complete_bin_tree_helper(tree.root)


if __name__ == "__main__":
    tree = BinaryTree()

    tree.root = Node(1)

    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    tree.root.right.left = Node(6)

    print(get_num_node_complete_bin_tree(tree))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(log(n))
"""
