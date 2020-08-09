"""
Problem:

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.


EXAMPLE:

Input =
   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
Output =
   0
  / \
 1   0
    /
   1
(We do not remove the tree at the root or its left child because it still has a 1 as a descendant.)
"""

# local import from the Datastructure module
from DataStructures.Tree import Node, Binary_Tree

# helper function to prune the tree
def prune_helper(node):
    # checking if the left node is present
    if node.left:
        # pruning the left subtree
        prune_helper(node.left)

        # checking if the value of the left child is 0
        if node.left.val == 0:
            # if the value is 0 and its a leaf node, the node is deleted
            if not node.left.left and not node.left.right:
                temp = node.left
                node.left = None
                del temp

    # checking if the right node is present
    if node.right:
        # pruning the right subtree
        prune_helper(node.right)

        # checking if the value of the right child is 0
        if node.right.val == 0:
            # if the value is 0 and its a leaf node, the node is deleted
            if not node.right.left and not node.right.right:
                temp = node.right
                node.right = None
                del temp


# FUNCTION TO PERFORM THE OPERATION
def prune(tree):
    # checking if the tree has values and calling the helper function
    if tree.root:
        prune_helper(tree.root)
        return tree
    else:
        return None


# DRIVER CODE
tree = Binary_Tree()
tree.root = Node(0)
tree.root.left = Node(1)
tree.root.right = Node(0)
tree.root.right.left = Node(1)
tree.root.right.left.left = Node(0)
tree.root.right.left.right = Node(0)
tree.root.right.right = Node(0)

print(tree)
print(prune(tree))
