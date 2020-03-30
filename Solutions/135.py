'''
Problem:

Given a binary tree, find a minimum path sum from root to a leaf.

Example:

Input =   10
         /  \
        5    5
         \     \
           2    1
               /
             -1
Output = [10, 5, 1, -1] (sum 15)
'''

# local import from the Datastructure module
from DataStructures.Tree import Binary_Tree, Node

# helper function to perform the operations
def minimum_path_sum_helper(self):
    # getting the minimum sum for the left subtree
    if (self.left):
        left_sum, left = self.left.minimum_path_sum_helper()
    else:
        left_sum, left = None, None
    # getting the minimum sum for the right subtree
    if (self.right):
        right_sum, right = self.right.minimum_path_sum_helper()
    else:
        right_sum, right = None, None
    
    # if its a leaf node (base case for recursion), the value and a list containing the value is returned
    if (not left and not right):
        return self.val, [self.val]
    # if only left child is present, the updated values (updated using left sum and list) are returned
    elif (left and not right):
        return (left_sum+self.val), left+[self.val]
    # if only right child is present, the updated values (updated using right sum and list) are returned
    elif (right and not left):
        return (right_sum+self.val), right+[self.val]
    # if both children are present, the path with smaller sum is selected and values updated correspondingly
    else:
        if (left_sum < right_sum):
            return (left_sum+self.val), left+[self.val]
        else:
            return (right_sum+self.val), right+[self.val]

# FUNCTION TO PERFORM THE OPERATION     
def minimum_path_sum(self):
    # checking if the tree has nodes
    if (self.root):
        # getting the path from the leaf to root and returning the reverse
        _, path = self.root.minimum_path_sum_helper()
        return path[::-1]
    # raising ValueError in case the tree is empty
    else:
        raise ValueError("Empty Tree")

# adding the necessary functions to the classes
setattr(Node, 'minimum_path_sum_helper', minimum_path_sum_helper)
setattr(Binary_Tree, 'minimum_path_sum', minimum_path_sum)

# DRIVER CODE
tree = Binary_Tree()
tree.root = Node(10)
tree.root.left = Node(5, right=Node(2))
tree.root.right = Node(5, right=Node(1, left=Node(-1)))

print(tree)
print(tree.minimum_path_sum())