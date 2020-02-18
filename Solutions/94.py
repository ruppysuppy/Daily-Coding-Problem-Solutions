'''
Problem:

Given a binary tree of integers, find the maximum path sum between two nodes. 
The path must go through at least one node, and does not need to go through the root.
'''

#local imports from DataStructure
from DataStructures.Tree import Node, Binary_Tree

# helper function to do the heavy-lifting
def get_max_path_sum_helper(node, current_max_sum, overall_max_sum):
    # if the node is None (empty tree/ leaf's children), the path sum is 0
    if (not node):
        return 0
    
    # getting the left and right max path sum
    l_max_sum = get_max_path_sum_helper(node.left, current_max_sum, overall_max_sum)
    r_max_sum = get_max_path_sum_helper(node.right, current_max_sum, overall_max_sum)

    # current sum is the max of (
    #                           current sum + node's val [node is added to the current sum]
    #                           current sum [node is not used to form the current max sum]
    #                           node's val [only the node is selected]
    #                           left max sum + node's val [the right subtree is not selected]
    #                           right max sum + node's val [the left subtree is not selected]
    #                           left max sum + node's val + right max sum [the entire subtree is selected]
    #                           )
    current_max_sum = max(current_max_sum+node.val, current_max_sum, node.val, l_max_sum+node.val, r_max_sum+node.val, l_max_sum+node.val+r_max_sum)
    # overall max sum is updated as per requirement
    overall_max_sum = max(current_max_sum, overall_max_sum)

    return overall_max_sum

# FUNCTION TO PERFORM THE OPERATION
def get_max_path_sum(self):
    return get_max_path_sum_helper(self.root, 0, 0)

# attaching the function to the Binary_Tree class
setattr(Binary_Tree, 'get_max_path_sum', get_max_path_sum)

# DRIVER CODE
tree = Binary_Tree()
tree.root = Node(1)

print(tree)
print(tree.get_max_path_sum())

tree.root.left = Node(2)
print(tree)
print(tree.get_max_path_sum())

tree.root.right = Node(3)
print(tree)
print(tree.get_max_path_sum())

tree.root.val = -1
print(tree)
print(tree.get_max_path_sum())

tree.root.left.left = Node(4)
print(tree)
print(tree.get_max_path_sum())