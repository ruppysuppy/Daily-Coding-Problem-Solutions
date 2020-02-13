'''
Problem:

Determine whether a tree is a valid binary search tree.
A binary search tree is a tree with two children, left and right, and satisfies the BST constraint.

BST constraint: the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
'''

# importing tree from datastructure
from DataStructures.Tree import Binary_Tree, Binary_Search_Tree, Node

# helper function for the main operation
def bst_check_helper(node):
   # if the passed node (only applicable for the root) is empty, True is returned [recursion base case]
   if (node == None):
      return True
   
   # if its a leaf node, True is returned [recursion base case]
   if (node.left == None and node.right == None):
      return True
   # if the children nodes exist but doesn't follow the BST constraint, False is returned
   elif ((node.left and node.left.val > node.val) or (node.right and node.right.val < node.val)):
      return False
   # returning the value for the bst check on both left and right children
   return (bst_check_helper(node.left) and bst_check_helper(node.right))

# FUNCTION TO PERFORM THE OPERATION
def bst_check(tree):
   return bst_check_helper(tree.root)

# DRIVER CODE
tree = Binary_Search_Tree()
tree.add(5)
tree.add(9)
tree.add(1)
tree.add(4)
tree.add(10)
tree.add(3)
tree.add(2)
tree.add(10)
tree.add(7)
print(f"BST Check Status: {bst_check(tree)}")

tree = Binary_Search_Tree()
print(f"BST Check Status: {bst_check(tree)}")

tree = Binary_Tree(5)
tree.root.left = Node(5)
tree.root.right = Node(5)
print(f"BST Check Status: {bst_check(tree)}")

tree = Binary_Tree(5)
tree.root.left = Node(6)
tree.root.right = Node(5)
print(f"BST Check Status: {bst_check(tree)}")