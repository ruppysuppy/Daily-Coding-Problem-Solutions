"""
Problem:

Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

Example:

Input = [2, 4, 3, 8, 7, 5]
Output =
    5
   / \
  3   7
 / \   \
2   4   8
"""

# importing the required classes from the Datastructures module
from DataStructures.Tree import Binary_Search_Tree, Node

# construct (helper function)
def construct(tree, postorder):
    # each node is added to the tree
    for val in postorder:
        tree.add(val)


# FUNCTION TO PERFORM THE OPERATION
def bst_from_postorder(postorder):
    # creating the bst
    tree = Binary_Search_Tree()

    # if there are elements in the postorder traversal
    # the root is added and the construct function is called to create the rest of the tree
    # (reversed postorder array is passed excluding the root element)
    if postorder:
        tree.add(postorder[-1])
        construct(tree, postorder[-2::-1])

    return tree


# DRIVER CODE
print(bst_from_postorder([2, 4, 3, 8, 7, 5]))
