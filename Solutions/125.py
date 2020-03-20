'''
Problem:

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.


EXAMPLE:

Input = 20,      10
               /   \
             5      15
                   /  \
                 11    15
Output = 5, 15
'''

# local import from the Datastructure module
from DataStructures.Tree import Binary_Tree, Node

# traversal helper function for the node class (generator function for inorder traversal)
def traverse_helper(self):
    # if left child exists
    if (self.left):
        # the function is called recursively to generate all children
        for val in self.left.traverse_helper():
            # the node's value is yielded (to keep the function in memory)
            yield val
    
    # the current node's value is yielded (to keep the function in memory)
    yield self.val

    # if right child exists
    if (self.right):
        # the function is called recursively to generate all children
        for val in self.right.traverse_helper():
            # the node's value is yielded (to keep the function in memory)
            yield val

# traverse function for the tree class
def traverse(self):
    # the tree has nodes, the traversal enerator is returned
    if (self.root):
        return self.root.traverse_helper()
    # None is returned if the tree is empty
    return None

# adding the necessary functions to the respective classes
setattr(Node, 'traverse_helper', traverse_helper)
setattr(Binary_Tree, 'traverse', traverse)

# FUNCTION TO PERFORM THE OPERATION
def get_target_sum(tree, k):
  # getting the generator
    generator = tree.traverse()

    # if the generator is None, the tree is empty, None is returned
    if (not generator):
        return None
    
    # previous is a set of previously seen values
    previous = set()

    # getting the values from the generator
    for val in generator:
        # if (k - val) is in the set, (k - val) and the current value is returned
        if ((k - val) in previous):
            return (k - val), val
        # if (k - val) is not found, the current valu is added to the set
        previous.add(val)
    
    # if the target sum cannot be reached by 2 values in the tree, a tuple of 2 None is returned
    return None, None

# DRIVER CODE
tree = Binary_Tree()
tree.root = Node(10)
tree.root.left = Node(5)
tree.root.right = Node(15)
tree.root.right.left = Node(11)
tree.root.right.right = Node(15)

print(get_target_sum(tree, 15))
print(get_target_sum(tree, 20))
print(get_target_sum(tree, 21))
print(get_target_sum(tree, 25))
print(get_target_sum(tree, 30))
print(get_target_sum(tree, 35))