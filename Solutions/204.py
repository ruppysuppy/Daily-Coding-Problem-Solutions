'''
Problem:

Given a complete binary tree, count the number of nodes in faster than O(n) time. 
Recall that a complete binary tree has every level filled except the last, and the nodes in the last level are filled starting from the left.
'''

# local import from the Datastructure class
from DataStructures.Tree import Binary_Tree, Node

# helper function to get the number of nodes
def get_num_node_complete_bin_tree_helper(self, left_route_levels=0, right_route_levels=0):
    # getting the number of levels in the left sub-tree (runs in the 1st call only)
    if (not left_route_levels):
        node = self

        while (node):
            node = node.left
            left_route_levels += 1
    
    # getting the number of levels in the right sub-tree (runs in the 1st call only)
    if (not right_route_levels):
        node = self

        while (node):
            node = node.right
            right_route_levels += 1
    
    # checking if the binary tree is completely filled
    if (left_route_levels == right_route_levels):
        return 2 ** left_route_levels - 1
    
    # getting the number of nodes in the left sub-tree
    if (self.left):
        left_route_nodes = self.left.get_num_node_complete_bin_tree_helper(left_route_levels-1, 0)
    else:
        left_route_nodes = 0
    # getting the number of nodes in the right sub-tree
    if (self.right):
        right_route_nodes = self.right.get_num_node_complete_bin_tree_helper(0, right_route_levels-1)
    else:
        right_route_nodes = 0

    # returning the total nodes in the current sub-tree
    return left_route_nodes + right_route_nodes + 1

# adding the function to the Node class
setattr(Node, 'get_num_node_complete_bin_tree_helper', get_num_node_complete_bin_tree_helper)

# FUNCTION TO PERFORM THE OPERATION
def get_num_node_complete_bin_tree(tree):
    # returning 0 if the tree is empty
    if (not tree.root):
        return 0
    # getting the number of nodes using the helper function
    return tree.root.get_num_node_complete_bin_tree_helper()

# DRIVER CODE
tree = Binary_Tree()

tree.root = Node(1)

tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)

print(get_num_node_complete_bin_tree(tree))