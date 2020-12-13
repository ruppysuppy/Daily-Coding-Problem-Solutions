"""
Problem:

Given a binary tree of integers, find the maximum path sum between two nodes. The path
must go through at least one node, and does not need to go through the root.
"""

from DataStructures.Tree import BinaryTree, Node


def get_max_path_sum_helper(
    node: Node, current_max_sum: int = 0, overall_max_sum: int = 0
) -> int:
    if not node:
        return 0

    l_max_sum = get_max_path_sum_helper(node.left, current_max_sum, overall_max_sum)
    r_max_sum = get_max_path_sum_helper(node.right, current_max_sum, overall_max_sum)
    # current max sum = max(
    #   node's value added to the current sum
    #   current max sum
    #   only node's value selected
    #   right subtree not selected
    #   left subtree not selected
    #   entire subtree selected
    #   )
    current_max_sum = max(
        current_max_sum + node.val,
        current_max_sum,
        node.val,
        l_max_sum + node.val,
        r_max_sum + node.val,
        l_max_sum + node.val + r_max_sum,
    )
    # overall max sum is updated as per requirement
    overall_max_sum = max(current_max_sum, overall_max_sum)
    return overall_max_sum


def get_max_path_sum(tree: BinaryTree) -> int:
    return get_max_path_sum_helper(tree.root)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)

    print(tree)
    print(get_max_path_sum(tree))

    tree.root.left = Node(2)
    print(tree)
    print(get_max_path_sum(tree))

    tree.root.right = Node(3)
    print(tree)
    print(get_max_path_sum(tree))

    tree.root.val = -1
    print(tree)
    print(get_max_path_sum(tree))

    tree.root.left.left = Node(4)
    print(tree)
    print(get_max_path_sum(tree))

    tree.root.right.right = Node(-1)
    print(tree)
    print(get_max_path_sum(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n))
"""
