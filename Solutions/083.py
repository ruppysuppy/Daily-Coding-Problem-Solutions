"""
Problem:

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""

from DataStructures.Tree import BinaryTree, Node


def invert_helper(node: Node) -> None:
    node.right, node.left = node.left, node.right
    # recursively inverting the children
    if node.right is not None:
        invert_helper(node.right)
    if node.left is not None:
        invert_helper(node.left)


def invert(tree: BinaryTree) -> None:
    # inverts the tree in place
    if not tree.root:
        return
    invert_helper(tree.root)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node("a")

    tree.root.left = Node("b")
    tree.root.right = Node("c")

    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")

    tree.root.right.left = Node("f")

    print(tree)

    invert(tree)

    print(tree)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n))
"""
