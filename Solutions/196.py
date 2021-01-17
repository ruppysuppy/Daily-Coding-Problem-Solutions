"""
Problem:

Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of
a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5

Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
"""

from typing import Dict

from DataStructures.Tree import Node, BinaryTree


def add_to_freq_count(val: int, dictionary: Dict[int, int]) -> Dict[int, int]:
    if val not in dictionary:
        dictionary[val] = 0
    dictionary[val] += 1
    return dictionary


def get_frequent_subtree_sum_helper(
    node: Node, sum_freq: Dict[int, int] = {}
) -> Dict[int, int]:
    if node.left is None and node.right is None:
        return add_to_freq_count(node.val, sum_freq), node.val

    elif node.left is not None and node.right is None:
        sum_freq, current = get_frequent_subtree_sum_helper(node.left, sum_freq)
        current += node.val
        return add_to_freq_count(current, sum_freq), current

    elif node.left is None and node.right is not None:
        sum_freq, current = get_frequent_subtree_sum_helper(node.right, sum_freq)
        current += node.val
        return add_to_freq_count(current, sum_freq), current

    sum_freq, current_left = get_frequent_subtree_sum_helper(node.left, sum_freq)
    sum_freq, current_right = get_frequent_subtree_sum_helper(node.right, sum_freq)
    current = current_left + node.val + current_right
    return add_to_freq_count(current, sum_freq), current


def get_frequent_subtree_sum(tree: BinaryTree) -> int:
    freq, _ = get_frequent_subtree_sum_helper(tree.root, {})
    # finding the most frequent value
    modal_value, frequency = None, 0
    for key, val in freq.items():
        if val > frequency:
            frequency = val
            modal_value = key
    return modal_value


if __name__ == "__main__":
    tree = BinaryTree()

    tree.root = Node(5)
    tree.root.left = Node(2)
    tree.root.right = Node(-5)

    print(tree)

    print(get_frequent_subtree_sum(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
