"""
Problem:

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. 
Assume that each node in the tree also has a pointer to its parent.
According to the definition of LCA on Wikipedia: 
"The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants.
(where we allow a node to be a descendant of itself)"
"""

# Node class for the nodes of the tree
class Node:
    # initialization
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    # string function
    def __str__(self):
        return self.to_str()

    # equality function
    def __eq__(self, other):
        return self is other

    # helper function to convert the tree into a string
    def to_str(self):
        if self.right == None and self.left == None:
            return f"('{self.val}')"
        elif self.left != None and self.right == None:
            return f"({self.left.to_str()}, '{self.val}', None)"
        elif self.left != None and self.right != None:
            return f"({self.left.to_str()}, '{self.val}', {self.right.to_str()})"
        elif self.left == None and self.right != None:
            return f"(None, '{self.val}', {self.right.to_str()})"


# Binary Tree class
class Binary_Tree:
    # initialization
    def __init__(self, val=None):
        if val != None:
            self.root = Node(val)
        else:
            self.root = None

    # string function
    def __str__(self):
        return str(self.root)


# FUNCTION TO PERFROM THE OPERATION
def get_lca(node1, node2):
    # depth1 and depth2 stores the depth at which node1 and node2 are located
    depth1 = 0
    depth2 = 0

    # pos pointer to traverse the tree to the root (node1)
    pos = node1

    # traversing to the root and getting the depth
    while pos.parent:
        pos = pos.parent
        depth1 += 1

    # storing the root in temp
    temp = pos

    # pos pointer to traverse the tree to the root (node2)
    pos = node2

    # traversing to the root and getting the depth
    while pos.parent:
        pos = pos.parent
        depth2 += 1

    # if the nodes reside in different trees, None is returned
    if not (temp == pos):
        return None

    # pointers to get the current poistion during the traversal for each node
    pos1 = node1
    pos2 = node2

    # moving pos1 to the correct position for comparision
    if depth1 > depth2:
        for _ in range(depth1 - depth2):
            pos1 = pos1.parent
    # moving pos2 to the correct position for comparision
    else:
        for _ in range(depth2 - depth1):
            pos2 = pos2.parent

    # comparing the values of the pointers to find the correct position
    while pos1:
        if pos1 == pos2:
            return pos1.val

        pos1 = pos1.parent
        pos2 = pos2.parent


# DRIVER CODE
tree = Binary_Tree()
a = Node(1)
b = Node(2, parent=a)
c = Node(3, parent=a)
d = Node(4, parent=b)
e = Node(5, parent=b)
f = Node(6, parent=c)
g = Node(7, parent=c)

tree.root = a
tree.root.left = b
tree.root.right = c
tree.root.left.left = d
tree.root.left.right = e
tree.root.right.left = f
tree.root.right.right = g

print(tree)

print(get_lca(f, g))
print(get_lca(a, g))
print(get_lca(d, g))
print(get_lca(a, c))
print(get_lca(e, b))
