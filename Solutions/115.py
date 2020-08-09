"""
Problem:

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants. 
The tree s could also be considered as a subtree of itself.
"""

# local import from DataStructures module
from DataStructures.Tree import Binary_Tree, Node

# equality function for Node class (checks the entire subtree)
def __eq__(self, other):
    # checking if any of the node is empty or other's type is a mismatch
    if (not self) or (not other) or (type(other) != Node):
        return False

    # if the values they hold are different, False is returned
    if self.val != other.val:
        return False

    # returning the value for the similarity of the children (recursive)
    return self.left == other.left and self.right == other.right


# helper function to all occourances where the value is same
def find_helper(self, tree_search):
    # checking the equality of the subtree
    if self == tree_search:
        return True

    # if the subtree was not same, the children are checked
    if self.left and self.left.find_helper(tree_search):
        return True
    if self.right and self.right.find_helper(tree_search):
        return True

    # if no match was found, False is returned
    return False


# function to perform the pre-requisite checks and calling the find_helper
def match(self, other):
    # checking if the other object has the same class and has a root Node and the tree has a root node too, the result of the check is returned
    if type(other) == Binary_Tree and other.root and self.root:
        return self.root.find_helper(other.root)
    # else False is returned
    else:
        return False


# adding the custom created functions to the classes
setattr(Node, "__eq__", __eq__)
setattr(Node, "find_helper", find_helper)
setattr(Binary_Tree, "match", match)

# FUNCTION TO PERFORM THE OPERATION
def get_match(s, t):
    return s.match(t)


# DRIVER CODE
tree1 = Binary_Tree()
tree1.root = Node(0)
tree1.root.left = Node(1)
tree1.root.right = Node(2)
tree1.root.right.left = Node(3)
tree1.root.right.right = Node(4)

tree2 = Binary_Tree()
tree2.root = Node(2)
tree2.root.left = Node(3)
tree2.root.right = Node(4)

tree3 = Binary_Tree()
tree3.root = Node(2)
tree3.root.left = Node(3)
tree3.root.right = Node(5)

print(get_match(tree1, tree2))
print(get_match(tree1, tree3))
