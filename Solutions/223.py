"""
Problem:

Typically, an implementation of in-order traversal of a binary tree has O(h) space
complexity, where h is the height of the tree. Write a program to compute the in-order
traversal of a binary tree using O(1) space.
"""

from typing import Generator

from DataStructures.Tree import BinaryTree, Node


def morris_traversal(tree: BinaryTree) -> Generator[int, None, None]:
    current = tree.root

    while current is not None:
        if current.left is None:
            yield current.val
            current = current.right
            continue
        # Find the inorder predecessor of current
        pre = current.left
        while pre.right is not None and pre.right is not current:
            pre = pre.right
        if pre.right is None:
            # Make current as right child of its inorder predecessor
            pre.right = current
            current = current.left
        else:
            # Revert the changes made in the 'if' part to restore the
            # original tree. (Fix the right child of predecessor)
            pre.right = None
            yield current.val
            current = current.right


if __name__ == "__main__":
    tree = BinaryTree()

    tree.root = Node(1)

    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    tree.root.right.right = Node(6)

    print(tree)
    for node in morris_traversal(tree):
        print(node, end=" ")


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
