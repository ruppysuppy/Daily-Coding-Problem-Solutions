"""
Problem:

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]
And the following inorder traversal:

[d, b, e, a, f, c, g]
You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
"""

from typing import List

from DataStructures.Tree import BinaryTree, Node


def generate_tree(preorder: List[int], inorder: List[int]) -> BinaryTree:
    length = len(preorder)
    if length != len(inorder):
        raise RuntimeError
    if length == 0:
        return BinaryTree()
    # generating the root
    root = preorder[0]
    tree = BinaryTree()
    tree.root = Node(root)
    # generating the rest of the tree
    if length > 1:
        i = inorder.index(root)
        # partitioning the nodes as per the branch
        inorder_left, preorder_left = (inorder[:i], preorder[1 : i + 1])
        inorder_right, preorder_right = (inorder[i + 1 :], preorder[i + 1 :])
        # creating a tree for each branch
        tree_left = generate_tree(preorder_left, inorder_left)
        tree_right = generate_tree(preorder_right, inorder_right)
        # attaching the sub-tree to their respective branch
        tree.root.left = tree_left.root
        tree.root.right = tree_right.root
    return tree


if __name__ == "__main__":
    test1 = generate_tree(
        ["a", "b", "d", "e", "c", "f", "g"], ["d", "b", "e", "a", "f", "c", "g"]
    )
    print(test1)

    test2 = generate_tree(
        ["a", "b", "d", "e", "c", "f"], ["d", "b", "e", "a", "f", "c"]
    )
    print(test2)


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
