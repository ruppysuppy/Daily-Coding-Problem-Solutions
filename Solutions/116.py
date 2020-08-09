"""
Problem:

Generate a finite, but an arbitrarily large binary tree quickly in O(1).
That is, generate() should return a tree whose size is unbounded but finite.
"""

# local import from the DataStructures module
from DataStructures.Tree import Node, Binary_Tree

# library imports
from random import random, randint

# matplotlib is used to plot the distribution (not mandatory)
import matplotlib.pyplot as plt

# helper function to generate the random branches
def generate_helper(self, probability=0.5, probability_branch=0.5):
    # generating a random number
    prob_res = random()

    # if the number is larger than the probabilty, the branch generation is stopped
    if prob_res > probability:
        return

    # generating random numbers for left and right branch
    prob_res_left = random()
    prob_res_right = random()

    # generating the left branch based on probability
    if prob_res_left < probability_branch:
        self.left = Node(randint(1, 1000))
        self.left.generate_helper(probability, probability_branch)
    # generating the right branch based on probability
    if prob_res_right < probability_branch:
        self.right = Node(randint(1, 1000))
        self.right.generate_helper(probability, probability_branch)


# len function helper (member of Node class)
def tree_length_helper(self):
    # getting the the left height
    if self.left:
        left = self.left.tree_length_helper()
    else:
        left = 0

    # getting the the right height
    if self.right:
        right = self.right.tree_length_helper()
    else:
        right = 0

    # returning the sum of left, right and 1 (as the subtree consists of left and right children and the node itself)
    return left + right + 1


# len function for the binary tree class
def __len__(self):
    if self.root:
        return self.root.tree_length_helper()
    return 0


# adding the necessary functions to the classses
setattr(Node, "generate_helper", generate_helper)
setattr(Node, "tree_length_helper", tree_length_helper)
setattr(Binary_Tree, "__len__", __len__)

# FUNCTION TO PERFORM THE OPERATION
def generate():
    # creating the binary tree
    tree = Binary_Tree()

    # adding the root node and generating the random branches
    tree.root = Node(randint(1, 1000))
    tree.root.generate_helper(0.7, 0.7)

    # returning the tree
    return tree


# DRIVER CODE
res = []

for i in range(1000):
    res.append(len(generate()))

plt.xlim(right=2500, left=100)
plt.ylim(top=100)
plt.hist(res, bins=50)
plt.show()
