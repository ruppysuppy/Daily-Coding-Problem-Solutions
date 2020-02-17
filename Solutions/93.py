'''
Problem:

Given a tree, find the largest tree/subtree that is a BST.
Given a tree, return the size of the largest tree/subtree that is a BST.
'''

# local import from the DataStructres class
from DataStructures.Tree import Binary_Tree, Node

# function do perform the main heavylifting
def get_largest_bst_size_helper(node):
    # base case 1 of recursion (node is None)
    if (not node):
        return 0, node, True, 999999, -999999

    # base case 1 of recursion (leaf node)
    if (not node.left and not node.right):
        return 1, node, True, node.val, node.val

    # getting the left and right results (height of largest bst, root of largest bst, if the entire sub-tree (left/right) is a bst, max value in the largest bst, min value in the largest bst)
    l_height, l_root, l_is_bst, l_max_val, l_min_val = get_largest_bst_size_helper(node.left)
    r_height, r_root, r_is_bst, r_max_val, r_min_val = get_largest_bst_size_helper(node.right)

    # if both the left & right sub-trees are bst
    if (l_is_bst and r_is_bst):
        # if both the left and right nodes exist
        if (node.left and node.right):
            # checking for bst condition
            if (node.val > l_max_val and node.val < r_min_val):
                return (l_height+r_height+1), node, True, r_max_val, l_min_val
        else:
            # if the left node exists, if the bst condition is met, the values are returned
            if (node.left and node.val > l_max_val):
                return l_height+1, node, True, node.val, l_min_val
            # if the right node exist, if the bst condition is met, the values are returned
            elif (node.right and node.val < r_min_val):
                return r_height+1, node, True, r_max_val, node.val
    
    # if either of the left or right sub-trees is not a bst, the larger one is returned
    if (l_height > r_height):
        return l_height, l_root, False, l_max_val, l_min_val
    else:
        return r_height, r_root, False, r_max_val, r_min_val

# FUNCTION TO PERFORM THE OPERATION
def get_largest_bst_size(self):
    size, node, _, _, _ = get_largest_bst_size_helper(self.root)
    return size, node.val

# adding the fucntion to the Binary_Tree class
setattr(Binary_Tree, 'get_largest_bst_size', get_largest_bst_size)

# DRIVER CODE
a = Node(3)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(1)
f = Node(4)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
tree = Binary_Tree()
tree.root = a

print(tree)
print("Size: {}\tNode Val: {}".format(*tree.get_largest_bst_size()))

a = Node(3)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(4)
f = Node(4)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
tree = Binary_Tree()
tree.root = a

print(tree)
print("Size: {}\tNode Val: {}".format(*tree.get_largest_bst_size()))

a = Node(1)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(3)
f = Node(4)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
tree = Binary_Tree()
tree.root = a

print(tree)
print("Size: {}\tNode Val: {}".format(*tree.get_largest_bst_size()))

a = Node(3)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(3)
f = Node(4)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
tree = Binary_Tree()
tree.root = a

print(tree)
print("Size: {}\tNode Val: {}".format(*tree.get_largest_bst_size()))

a = Node(3)
b = Node(1)
c = Node(6)
d = Node(0)
e = Node(2)
f = Node(4)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
tree = Binary_Tree()
tree.root = a

print(tree)
print("Size: {}\tNode Val: {}".format(*tree.get_largest_bst_size()))