"""
Problem:

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees
containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:

   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a
descendant.
"""

from DataStructures.Tree import Node, BinaryTree


def prune_helper(node: Node) -> None:
    if node.left:
        prune_helper(node.left)
        if node.left.val == 0:
            if not node.left.left and not node.left.right:
                temp = node.left
                node.left = None
                del temp
    if node.right:
        prune_helper(node.right)
        if node.right.val == 0:
            if not node.right.left and not node.right.right:
                temp = node.right
                node.right = None
                del temp


def prune(tree: BinaryTree) -> BinaryTree:
    if tree.root:
        prune_helper(tree.root)
    return tree


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(0)

    tree.root.left = Node(1)
    tree.root.right = Node(0)

    tree.root.right.left = Node(1)
    tree.root.right.right = Node(0)

    tree.root.right.left.left = Node(0)
    tree.root.right.left.right = Node(0)

    print(tree)
    print(prune(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n))
"""
