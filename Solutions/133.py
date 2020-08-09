"""
Problem:

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor. 
You can assume each node has a parent pointer.

Example:

Input = 22, 
   10
  /  \
 5    30
     /  \
   22    35
Output = 30
"""

# local import from Datastructure class
from DataStructures.Tree import Node, Binary_Tree

# function to find the required node
def search(self, val):
    # if the node is found, its returned (base case for recursion)
    if self.val == val:
        return self

    # using the binary search tree property to execute binary search
    if val < self.val:
        if self.left:
            return self.left.search(val)
        # if the required node is not present, None is returned (base case for recursion)
        else:
            return None

    else:
        if self.right:
            return self.right.search(val)
        # if the required node is not present, None is returned (base case for recursion)
        else:
            return None


# helper function to compute the inorder successor
def inorder_successor_helper(self):
    # if the node has a right child, by bst property, the left-most node in the right subtree is the inorder sucessor
    if self.right:
        pos = self.right

        while pos.left:
            pos = pos.left

        return pos.val

    # if the node doesn't have a right child, the node's parent is the inorder sucessor
    else:
        if self.parent:
            return self.parent.val
        else:
            return None


# FUNCTION TO PERFORM THE OPERATION
def inorder_successor(self, val):
    # checking whether the tree has nodes
    if self.root:
        # getting the required node
        node = self.root.search(val)

        # getting the inorder successor
        if node:
            return node.inorder_successor_helper()
        else:
            raise Exception("Node not Found")

    else:
        raise Exception("Empty Tree")


# adding the necessary functions and data to the classes
setattr(Node, "parent", None)
setattr(Node, "search", search)
setattr(Node, "inorder_successor_helper", inorder_successor_helper)
setattr(Binary_Tree, "inorder_successor", inorder_successor)

# DRIVER CODE
root = Node(10)
root.left = Node(5)
root.right = Node(30)
root.left.parent = root
root.right.parent = root
root.right.left = Node(22)
root.right.right = Node(35)
root.right.left.parent = root.right
root.right.right.parent = root.right

tree = Binary_Tree()
tree.root = root

print(tree)
print(tree.inorder_successor(22))
print(tree.inorder_successor(10))
