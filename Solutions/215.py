"""
Problem:

The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.
More rigorously, we can define it as follows:
* The horizontal distance of the root is 0.
* The horizontal distance of a left child is hd(parent) - 1.
* The horizontal distance of a right child is hd(parent) + 1.
For example, for the following tree, hd(1) = -2, and hd(6) = 0.
             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
The bottom view of a tree, then, consists of the lowest node at each horizontal distance. 
If there are two nodes at the same depth and horizontal distance, either is acceptable.
Given the root to a binary tree, return its bottom view.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].
"""

# importing from the local Datastructure module
from DataStructures.Tree import Node, Binary_Tree

# helper function to construct the bottom view
def get_bottom_view_helper(node, depth, hd, accumulator):
    # checking and adding the depth and value of the node as per requirement
    if hd not in accumulator:
        accumulator[hd] = (depth, node.val)
    else:
        if accumulator[hd][0] < depth:
            accumulator[hd] = (depth, node.val)

    # recursively calling the function for the children if they exist
    if node.left:
        get_bottom_view_helper(node.left, depth + 1, hd - 1, accumulator)
    if node.right:
        get_bottom_view_helper(node.right, depth + 1, hd + 1, accumulator)

    # returning the accumulator
    return accumulator


# FUNCTION TO PERFORM THE OPERATION
def get_bottom_view(tree):
    # getting the depth and value of each node by horizontal distance
    data = get_bottom_view_helper(tree.root, 0, 0, {})

    # creating a array for the data by the deepest nodes' horizontal distance
    res_arr = [(hd, data[hd][1]) for hd in data]
    # sorting the list by horizontal distance
    res_arr.sort(key=lambda elem: elem[0])

    # returning the bottom view (only the values)
    return [elem for _, elem in res_arr]


# DRIVER CODE
tree = Binary_Tree()
tree.root = Node(5)

tree.root.left = Node(3)
tree.root.right = Node(7)

tree.root.left.left = Node(1)
tree.root.left.right = Node(4)

tree.root.right.left = Node(6)
tree.root.right.right = Node(9)

tree.root.left.left.left = Node(0)

tree.root.right.right.left = Node(8)

print(tree)
print(get_bottom_view(tree))
