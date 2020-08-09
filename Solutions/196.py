"""
Problem:

Given the root of a binary tree, find the most frequent subtree sum. 
The subtree sum of a node is the sum of all values under a node, including the node itself.

Example:

Tree = 
  5
 / \
2  -5
Output = 2 (as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5)
"""

# importing from the Datastructure module
from DataStructures.Tree import Node, Binary_Tree

# function to count the frequency of a value
def add_to_freq_count(val, dictionary):
    if val in dictionary:
        dictionary[val] += 1
    else:
        dictionary[val] = 1
    return dictionary


# helper function to get the freqency
def get_frequent_subtree_sum_helper(self, sum_freq={}):
    # checking if the node is a leaf node
    if self.left == None and self.right == None:
        # adding the leaf value to the frequency and returning in the format (freq, current_sum)
        return add_to_freq_count(self.val, sum_freq), self.val

    # checking if the node has a left child but not the right child
    elif self.left != None and self.right == None:
        # getting the left frequency and the left sum
        sum_freq, current = self.left.get_frequent_subtree_sum_helper(sum_freq)
        # getting the current sum
        current += self.val
        # adding the value to the frequency and returning in the format (freq, current_sum)
        return add_to_freq_count(current, sum_freq), current

    # checking if the node has a right child but not the left child
    elif self.left == None and self.right != None:
        # getting the left frequency and the left sum
        sum_freq, current = self.right.get_frequent_subtree_sum_helper(sum_freq)
        # getting the current sum
        current += self.val
        # adding the value to the frequency and returning in the format (freq, current_sum)
        return add_to_freq_count(current, sum_freq), current

    # if the node has both children
    elif self.left != None and self.right != None:
        # getting the frequency and the sum for left and right sub-trees
        sum_freq, current_left = self.left.get_frequent_subtree_sum_helper(sum_freq)
        sum_freq, current_right = self.right.get_frequent_subtree_sum_helper(sum_freq)

        # getting the current sum
        current = current_left + self.val + current_right
        # adding the value to the frequency and returning in the format (freq, current_sum)
        return add_to_freq_count(current, sum_freq), current


# FUNCTION TO PERFORM THE OPERATION
def get_frequent_subtree_sum(self):
    # getting the frequency dictionary
    freq, _ = self.root.get_frequent_subtree_sum_helper({})
    # initializing res and frequency
    res = None
    frequency = 0

    # finding the most frequent value
    for key, val in freq.items():
        if val > frequency:
            frequency = val
            res = key
    # returning the most frequent value
    return res


# adding the functions to the necessary classes
setattr(Node, "get_frequent_subtree_sum_helper", get_frequent_subtree_sum_helper)
setattr(Binary_Tree, "get_frequent_subtree_sum", get_frequent_subtree_sum)

# DRIVER CODE
tree = Binary_Tree()

tree.root = Node(5)
tree.root.left = Node(2)
tree.root.right = Node(-5)

print(tree)

print(tree.get_frequent_subtree_sum())
