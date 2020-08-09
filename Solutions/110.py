"""
Problem:

Given a binary tree, return all paths from the root to leaves.

Example:

Input =    1
          / \
         2   3
            / \
           4   5
Output = [[1, 2], [1, 3, 4], [1, 3, 5]]"""

# local import from the DataStructures module
from DataStructures.Tree import Binary_Tree, Node

# helper function to do the heavy-lifting (part of Node class)
def get_paths_helper(self, res, temp):
    # if a leaf node is reached
    if not self.left and not self.right:
        # the leaf's value is added to temp
        temp.append(self.val)
        # a deep copy of temp is added to res
        res.append(list(temp))
        # the value of the leaf is poped from temp
        temp.pop()
    # if the node is not a leaf
    else:
        # the node's value is added to temp
        temp.append(self.val)
        # if the node has a left child, the function is recursively called on left child
        if self.left:
            self.left.get_paths_helper(res, temp)
        # if the node has a right child, the function is recursively called on right child
        if self.right:
            self.right.get_paths_helper(res, temp)
        # the node's value is removed from temp
        temp.pop()


# FUNCTION TO PERFORM THE OPERATION
def get_paths(self):
    # res stores the values from root to leaves
    res = []
    # calling the helper function on the root
    self.root.get_paths_helper(res, [])
    # returning res
    return res


# adding the necessary functions to their respective classes
setattr(Node, "get_paths_helper", get_paths_helper)
setattr(Binary_Tree, "get_paths", get_paths)

# DRIVER CODE
tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.left = Node(4)
tree.root.right.right = Node(5)

print(tree)
print(tree.get_paths())
