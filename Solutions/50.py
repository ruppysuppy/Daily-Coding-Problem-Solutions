"""
Problem:

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'
Given the root to such a tree, write a function to evaluate it.

Example:
    *
   / \
  +    +
 / \  / \
3  2  4  5
=> 45 [(3 + 2) * (4 + 5)]
"""

# local imports
from DataStructures.Tree import Binary_Tree, Node

# functions for operations to be performed
# addition
def add(num1, num2):
    return num1 + num2


# subtraction
def sub(num1, num2):
    return num1 - num2


# multiplication
def mul(num1, num2):
    return num1 * num2


# division
def div(num1, num2):
    return num1 / num2


# mapping the functions to the corresponding symbols
OPERATIONS_DICT = {"+": add, "-": sub, "*": mul, "/": div}

# modified node class to incorporate transform and calculate functions
class Node_modified(Node):
    # using default init
    def __init__(self, val, left=None, right=None):
        Node.__init__(self, val, left, right)

    # transform helper function: transforms the symbols to the corresponding function from the mapping
    def transform(self):
        # if the symbol is in the map, the value of the node is overwritten with the function
        if self.val in OPERATIONS_DICT:
            self.val = OPERATIONS_DICT[self.val]

            # recursive call on children (can only happen if its a valid operation)
            self.left.transform()
            self.right.transform()

    # actual function to calculate the result from the expression tree
    def calculate(self):
        # if the current node holds a function, its applied on its children recursively
        if callable(self.val):
            return self.val(self.left.calculate(), self.right.calculate())
        # if the current node holds a value, its returned
        else:
            return self.val


# FUNCTION TO PERFORM THE OPERATION
def calc(root):
    # if the root node is present (!= None), its transformed and the expression is calculated
    if root:
        root.transform()
        return root.calculate()
    # if root doesn't exist, None is returned
    else:
        return None


# DRIVER CODE
tree = Binary_Tree()
tree.root = Node_modified("*")
tree.root.left = Node_modified("+")
tree.root.right = Node_modified("+")
tree.root.left.left = Node_modified(3)
tree.root.left.right = Node_modified(2)
tree.root.right.left = Node_modified(4)
tree.root.right.right = Node_modified(5)

print(calc(tree.root))
