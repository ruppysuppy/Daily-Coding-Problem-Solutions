"""
Problem:

Given the root of a binary tree, return a deepest node.

Example:

Input =     a
           / \
          b   c
         /
        d
Output = d
"""

# local import
from DataStructures.Tree import Binary_Tree, Node

# helper function to do the heavy lifting
def deepest_node_helper(node):
    # the node is None, 0 and None is returned (base case of recursion)
    if not node:
        return 0, None

    # if its a leaf node, 1 and the node is returned (base case of recursion)
    if not (node.left or node.right):
        return 1, node

    # getting the left height and the deepest node of the left-subtree
    if node.left:
        left_height, left_node = deepest_node_helper(node.left)
    else:
        left_height, left_node = 0, None

    # getting the right height and the deepest node of the right-subtree
    if node.right:
        right_height, right_node = deepest_node_helper(node.right)
    else:
        right_height, right_node = 0, None

    # comparing the left and right heights and returning the deeper node and its height
    if left_height > right_height:
        return left_height + 1, left_node
    else:
        return right_height + 1, right_node


# FUNCTION TO PERFORM THE OPERATION
def deepest_node(tree):
    _, node = deepest_node_helper(tree.root)
    return node.val


# DRIVER CODE
tree = Binary_Tree("a")
tree.root.left = Node("b")
tree.root.right = Node("c")
tree.root.left.left = Node("d")

print(deepest_node(tree))
