'''
Problem:

Given a tree where each edge has a weight, compute the length of the longest path in the tree.
The path does not have to pass through the root, and each node can have any amount of children.

Example:

Input:
Tree =     a
          /|\
         b c d
            / \
           e   f
          / \
         g   h
weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1 
Output = 17 (the longest path would be c -> a -> d -> f, with a length of 17)
'''

# Node class
class Node:
    # initialization
    def __init__(self, val):
        self.val = val
        self.max_path = 0
        self.child_dists = {}
    
    # function to add a child to a node
    def add_children(self, child, wt):
        self.child_dists[child] = wt
    
    # function to get the max path (works only after updating the paths)
    def get_max_path(self, tree):
        # if the current node is a leaf, 0 is returned
        if (not self.child_dists):
            return 0
        
        # path_lengths store the max path length for the current node
        # children_max_path_lengths store the max path length for the current node's children
        path_lengths = []
        children_max_path_lengths = []

        # iterating throught the children of the current node and updating the arrays
        for node, dist in self.child_dists.items():
            path_lengths.append(tree.tree[node].max_path + dist)
            children_max_path_lengths.append(tree.tree[node].get_max_path(tree))
        
        # returning the result
        return max(sum(sorted(path_lengths)[-2:]), max(children_max_path_lengths))
    
    # function to update the paths
    def update_max_paths(self, tree):
        # max_path is set to 0 if the node has no children
        if (not self.child_dists):
            self.max_path = 0
            return

        # root_paths stores all the path length from the node to the leaves
        root_paths = list()

        # generating the root_paths
        for child, dist in self.child_dists.items():
            tree.tree[child].update_max_paths(tree)
            root_paths.append(tree.tree[child].max_path + dist)

        # storing the maximum root path
        self.max_path = max(root_paths)

# Tree class
class Tree:
    # initialization function
    def __init__(self):
        self.tree = {}
        self.root = None

    # function to add node to the tree
    def add_Node(self, val):
        self.tree[val] = Node(val)

        # incase the tree was empty, the passed node is stored as the root
        if (not self.root):
            self.root = val
    
    # add child function
    def add_child(self, parent, child, wt):
        # if the parent is absent ValueError is raised
        if (parent not in self.tree):
            raise ValueError("Parent Node not present in the tree")
            
        # the tree is created like a graph (with adjacency list)
        self.tree[parent].add_children(child, wt)
        self.tree[child] = Node(child)
    
    # get_longest_path function, updates the paths and calls get_max_path on root 
    # NOTE: if multiple times max path is run on the same tree, updating the paths once would suffice
    def get_longest_path(self):
        if (not self.root):
            return 0
        
        self.tree[self.root].update_max_paths(self)
        return self.tree[self.root].get_max_path(self)

# DRIVER CODE
tree = Tree()

tree.add_Node('a')
tree.add_child('a', 'b', 3)
tree.add_child('a', 'c', 5)
tree.add_child('a', 'd', 8)
tree.add_child('d', 'e', 2)
tree.add_child('d', 'f', 4)
tree.add_child('e', 'g', 1)
tree.add_child('e', 'h', 1)

print(tree.get_longest_path())