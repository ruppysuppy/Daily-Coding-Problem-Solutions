'''
Problem:

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

Example:
[a, b, d, e, c, f, g] (preorder), [d, b, e, a, f, c, g] (inorder) =>
    a
   / \
  b   c
 / \ / \
d  e f  g
'''

# Local Import from the datastructure module
from DataStructures.Tree import Binary_Tree, Node

# FUNCTION TO PERFORM THE OPERATION
def tree_gen(preorder, inorder):
    # Getting the number of nodes
    length = len(preorder)

    # if the preorder and inorder expressions has different number of nodes RuntimeError is raised
    if (length != len(inorder)):
        raise RuntimeError

    # if there are no nodes, an empty tree is returned
    if (length == 0):
        return Binary_Tree(None)
    
    # starting with the root
    root = preorder[0]
    tree = Binary_Tree(root)

    # if there are more nodes, the function is called recursively
    if (length > 1):
        # finding the index of the root in the inorder expression
        ind = inorder.index(root)

        # partitioning the nodes as per the branch
        temp_left = (inorder[:ind], preorder[1:ind+1])
        temp_right = (inorder[ind+1:], preorder[ind+1:])
        
        # creating a tree for each branch
        tree_left = tree_gen(temp_left[1], temp_left[0])
        tree_right = tree_gen(temp_right[1], temp_right[0])

        # attaching the sub-tree to their respective branch
        tree.root.left = tree_left.root
        tree.root.right = tree_right.root
    
    # the final tree is returned
    return tree

# DRIVER CODE
test1 = tree_gen(["a", "b", "d", "e", "c", "f", "g"], ["d", "b", "e", "a", "f", "c", "g"])
print(test1)

test2 = tree_gen(["a", "b", "d", "e", "c", "f"], ["d", "b", "e", "a", "f", "c"])
print(test2)