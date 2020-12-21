"""
Problem:

Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""

from random import random, randint

import matplotlib.pyplot as plt

from DataStructures.Tree import BinaryTree, Node


def generate_helper(
    node: Node,
    probability_add_children: float = 0.5,
    probability_add_branch: float = 0.5,
) -> None:
    if random() > probability_add_children:
        return
    # generating the left branch
    if random() < probability_add_branch:
        node.left = Node(randint(1, 1000))
        generate_helper(node.left, probability_add_children, probability_add_branch)
    # generating the right branch
    if random() < probability_add_branch:
        node.right = Node(randint(1, 1000))
        generate_helper(node.right, probability_add_children, probability_add_branch)


def generate() -> BinaryTree:
    tree = BinaryTree()
    tree.root = Node(randint(1, 1000))
    generate_helper(tree.root, 0.7, 0.7)
    # suggestion: don't use higher values for probability, it will lead to recursion
    # error
    return tree


if __name__ == "__main__":
    tree_length_list = []
    for i in range(1000):
        tree_length_list.append(len(generate()))
    plt.hist(tree_length_list)
    plt.show()


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
[n nodes cannot be generated in O(1) time, but since n is finite it may be considered
constant]
"""
