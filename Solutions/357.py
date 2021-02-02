"""
Problem:

You are given a binary tree in a peculiar string representation. Each node is written
in the form (lr), where l corresponds to the left child and r corresponds to the right
child.

If either l or r is null, it will be represented as a zero. Otherwise, it will be
represented by a new (lr) pair.

Here are a few examples:

A root node with no children: (00)
A root node with two children: ((00)(00))
An unbalanced tree with three consecutive left children: ((((00)0)0)0)
Given this representation, determine the depth of the tree.
"""


def get_depth(tree_representation: str) -> int:
    depth, max_depth = 0, 0
    for char in tree_representation:
        if char == "(":
            # entering a node (depth addition)
            depth += 1
        elif char == ")":
            # exiting a node (depth subtraction)
            depth -= 1
        max_depth = max(max_depth, depth)
    return max_depth


if __name__ == "__main__":
    print(get_depth("(00)"))
    print(get_depth("((00)(00))"))
    print(get_depth("((((00)0)0)0)"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
