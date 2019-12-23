'''
Problem:

Given the root to a binary search tree, find the second largest node in the tree.
'''

# Local Import from the datastructure module
from DataStructures.Tree import Node, Binary_Search_Tree

# Helper function to get the largest node and parent
def get_largest(node):
    # if there is no node, None is returned
    if (node == None):
        return None
    
    # parent is set to None (if the root is the largest node, parent is returned as None)
    parent = None

    # getting the right-most node (largest node as its a Binary Search Tree)
    while (node.right):
        parent = node
        node = node.right
    
    # both the parent and the node is returned
    return (parent, node)

# FUNCTION TO PERFORM THE OPERATION
def second_largest(tree):
    # if the tree is empty, None is returned
    if (tree.root == None):
        return None
    
    # finding the largest node
    largest_parent, largest = get_largest(tree.root)
    
    # if the largest node has a left node, the largest child of the left node is the 2nd largest node (BST property)
    if (largest.left):
        return (get_largest(largest.left)[1]).val
    
    # if the left node is absent and so is the parent (the tree contains only 1 node), None is returned
    elif (largest_parent == None):
        return None
    
    # if the largest parent is present its the 2nd largest node if no left node is present (BST property)
    return (largest_parent).val

# DRIVER CODE
tree = Binary_Search_Tree()
tree.add(5)
tree.add(3)
tree.add(8)
tree.add(2)
tree.add(4)
tree.add(7)
tree.add(9)

print(second_largest(tree))