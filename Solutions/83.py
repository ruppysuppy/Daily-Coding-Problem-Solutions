"""
Problem:

Invert a binary tree.

Example:

Input:
    a
   / \
  b   c
 / \  /
d   e f
Output:
  a
 / \
 c  b
 \  / \
  f e  d
"""

# importing from the local datastructure module
from DataStructures.Tree import Node, Binary_Tree

# function to do the heavy lifting
def invert_helper(self):
    # interchanging the left and right children
    self.right, self.left = self.left, self.right

    # if the right child exists, the function is recursively called on it (to interchange its children too)
    if self.right != None:
        self.right.invert_helper()

    # if the left child exists, the function is recursively called on it (to interchange its children too)
    if self.left != None:
        self.left.invert_helper()


# FUNCTION TO PERFORM THE OPERATION
def invert(self):
    self.root.invert_helper()


# adding the functions to the necessary class
setattr(Node, "invert_helper", invert_helper)
setattr(Binary_Tree, "invert", invert)

# DRIVER CODE
tree = Binary_Tree("a")
tree.root.left = Node("b")
tree.root.right = Node("c")
tree.root.left.left = Node("d")
tree.root.left.right = Node("e")
tree.root.right.left = Node("f")

print(tree)

tree.invert()

print(tree)
