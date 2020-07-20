'''
Problem:

Given a binary tree, determine whether or not it is height-balanced.
A height-balanced binary tree can be defined as one in which the heights of the two subtrees of any node never differ by more than one.
'''

from DataStructures.Tree import Node, Binary_Tree


def height_helper(self):
    # generating the left and right heights and the balance
    if self.left == None:
        left_height, balance_left = 0, True
    else:
        left_height, balance_left = self.left.height_helper()
    if self.right == None:
        right_height, balance_right = 0, True
    else:
        right_height, balance_right = self.right.height_helper()
    # returning the current balance factor and the balance check
    balance = balance_left and balance_right
    current_balance = -1 <= (right_height - left_height) <= 1
    height = max(left_height, right_height) + 1
    return height, balance and current_balance


def check_balance(self):
    _, balance = self.root.height_helper()
    return balance


# adding required methods to the classes
setattr(Node, 'height_helper', height_helper)
setattr(Binary_Tree, 'check_balance', check_balance)


# DRIVER CODE
tree = Binary_Tree()

tree.root = Node(0)
tree.root.left = Node(1)
tree.root.right = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)

print(tree.check_balance())

tree.root.left.right.left = Node(5)

print(tree.check_balance())
