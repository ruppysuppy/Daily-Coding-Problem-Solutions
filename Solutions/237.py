"""
Problem:

A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. 
The following tree is an example:
        4
      / | \
    3   5   3
  /           \
9              9
Given a k-ary tree, determine whether it is symmetric.
"""

# Node class to store a k-ary tree
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def __str__(self):
        return "{} -> {}".format(self.val, self.children)


def update_levels_dict(root, levels, lnum):
    # DFS to generate the nodes in the tree by level (stored in levels dictionary)
    if lnum not in levels:
        levels[lnum] = []
    levels[lnum].append(root.val)
    for child in root.children:
        update_levels_dict(child, levels, lnum + 1)


def is_symmetric(tree):
    # getting the nodes by the level number
    levels = {}
    update_levels_dict(tree, levels, 0)
    # checking if the tree is symmetric
    for level in levels:
        arr = levels[level]
        if arr != arr[::-1]:
            return False
    return True


# DRIVER CODE
a = Node(4)
b = Node(5)
c = Node(3)
d = Node(3)
e = Node(9)
f = Node(9)

a.children = [c, b, d]

c.children = [f]
d.children = [e]

print(is_symmetric(a))

c.children = [f, Node(1)]
d.children = [Node(1), e]

print(is_symmetric(a))

c.val = 4
print(is_symmetric(a))
