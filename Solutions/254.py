'''
Probelm:

Recall that a full binary tree is one in which each node is either a leaf node, or has two children. Given a binary tree, convert it to a full one by removing nodes with only one child.
For example, given the following tree:

         a
      /     \
    b         c
  /            \
d                 e
  \             /   \
    f          g     h
You should convert it to:
     a
  /     \
f         e
        /   \
       g     h
'''

from DataStructures.Tree import Node, Binary_Tree


def create_full_bin_tree_helper(self):
    # helper function to generate the full binary tree
    # if a node with one missing child is encountered, the value is replaced by its
    # child and the children of the current node overwrittrn with the child's children
    if self.right is None and self.left is None:
        return
    elif self.left is not None and self.right is None:
        self.val = self.left.val
        self.right = self.left.right
        self.left = self.left.left
        self.create_full_bin_tree_helper()
    elif self.left is None and self.right is not None:
        self.val = self.right.val
        self.left = self.right.left
        self.right = self.right.right
        self.create_full_bin_tree_helper()
    elif self.left is not None and self.right is not None:
        self.left.create_full_bin_tree_helper()
        self.right.create_full_bin_tree_helper()


def create_full_bin_tree(self):
    self.root.create_full_bin_tree_helper()


setattr(Node, 'create_full_bin_tree_helper', create_full_bin_tree_helper)
setattr(Binary_Tree, 'create_full_bin_tree', create_full_bin_tree)


# DRIVER CODE
tree = Binary_Tree()

tree.root = Node('a')
tree.root.left = Node('b')
tree.root.right = Node('c')

tree.root.left.left = Node('d')
tree.root.left.left.right = Node('f')

tree.root.right.right = Node('e')
tree.root.right.right.left = Node('g')
tree.root.right.right.right = Node('h')

print(tree)

tree.create_full_bin_tree()

print(tree)
