"""
Problem:

A unival tree (which stands for "universal value") is a tree where all nodes under it
have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

from typing import Tuple

from DataStructures.Tree import Node, BinaryTree


def num_universal_helper(node: Node, val: int, acc: int = 0) -> Tuple[int, bool]:
    # base case for recursion [leaf node]
    if node.left is None and node.right is None:
        if node.val == val:
            return (acc + 1), True
        return (acc + 1), False
    # if the value matches the parent's value, its children are also checked
    elif node.val == val:
        if node.left:
            acc, res1 = num_universal_helper(node.left, val, acc)
        else:
            res1 = True
        if node.right:
            acc, res2 = num_universal_helper(node.right, val, acc)
        else:
            res2 = True
        if res1 and res2:
            acc += 1
    # If the value doesn't match the parent's value, its children are checked with the
    # new value (value of the current node)
    else:
        if node.left:
            acc, res1 = num_universal_helper(node.left, node.val, acc)
        else:
            res1 = True
        if node.right:
            acc, res2 = num_universal_helper(node.right, node.val, acc)
        else:
            res2 = True
        if res1 and res2:
            acc += 1
    return acc, (node.val == val)


def num_universal(tree: BinaryTree) -> int:
    if not tree.root:
        return 0
    result, _ = num_universal_helper(tree.root, tree.root.val)
    return result


if __name__ == "__main__":
    tree = BinaryTree()

    tree.root = Node(0)
    tree.root.left = Node(1)
    tree.root.right = Node(0)

    tree.root.right.left = Node(1)
    tree.root.right.right = Node(0)

    tree.root.right.left.left = Node(1)
    tree.root.right.left.right = Node(1)

    print(tree)

    print(num_universal(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n)) [call stack]
"""
