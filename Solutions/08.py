'''
Problem:

Given a Binary tree, find the number of universal sub-trees.
An universal sub-tree is a sub tree, where the value of all the nodes is same.

Example:

Input =
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
Output = 5
'''

# Local Import from the datastructure module

from DataStructures.Tree import Node, Binary_Tree

# FUNCTION TO PERFORM THE OPERATION
def num_universal_helper(node, val, acc=0):
    # If the node is at the leaf 1 is added to the result (accumulator) and the value matches the parent's value, True is returned
    if (node.left == None and node.right == None):
        if (node.val == val):
            return (acc + 1), True
        else:
            return (acc + 1), False
    
    # If the value matches the parent's value, its children are also checked
    elif (node.val == val):
        if (node.left):
            acc, res1 = num_universal_helper(node.left, val, acc)
        else:
            res1 = True

        if (node.right):
            acc, res2 = num_universal_helper(node.right, val, acc)
        else:
            res2 = True
        
        if (res1 and res2):
            acc += 1
    
    # If the value doesn't match the parent's value, its children are also checked with the new value (value of the present node)
    else:
        if (node.left):
            acc, res1 = num_universal_helper(node.left, node.val, acc)
        else:
            res1 = True
            
        if (node.right):
            acc, res2 = num_universal_helper(node.right, node.val, acc)
        else:
            res2 = True
        
        if (res1 and res2):
            acc += 1
    
    return acc, (node.val == val)

# FUNCTION TO SIMPLIFY FUNCTION CALL OF NUM UNIVERSAL HELPER
def num_universal(tree):
    return num_universal_helper(tree.root, tree.root.val)[0]

# DRIVER CODE
tree = Binary_Tree(0)
tree.root.left = Node(1)
tree.root.right = Node(0)
tree.root.right.right = Node(0)
tree.root.right.left = Node(1)
tree.root.right.left.left = Node(1)
tree.root.right.left.right = Node(1)

print(tree)

print(num_universal(tree))