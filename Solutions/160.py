"""
Problem:

Given a tree where each edge has a weight, compute the length of the longest path in
the tree.

For example, given the following tree:

   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest
path would be c -> a -> d -> f, with a length of 17.

The path does not have to pass through the root, and each node can have any amount of
children.
"""

from __future__ import annotations


class Node:
    def __init__(self, val: str) -> None:
        self.val = val
        self.max_path = 0
        self.child_dists = {}

    def add_child(self, child: str, wt: int) -> None:
        self.child_dists[child] = wt

    def get_max_path(self, tree: Tree) -> int:
        if not self.child_dists:
            return 0
        # generating the max path length
        path_lengths = []
        children_max_path_lengths = []
        for node, dist in self.child_dists.items():
            path_lengths.append(tree.tree[node].max_path + dist)
            children_max_path_lengths.append(tree.tree[node].get_max_path(tree))
        return max(sum(sorted(path_lengths)[-2:]), max(children_max_path_lengths))

    def update_max_paths(self, tree: Tree) -> None:
        if not self.child_dists:
            self.max_path = 0
            return
        # generating the paths from the root
        root_paths = []
        for child, dist in self.child_dists.items():
            tree.tree[child].update_max_paths(tree)
            root_paths.append(tree.tree[child].max_path + dist)
        self.max_path = max(root_paths)


class Tree:
    def __init__(self) -> None:
        self.tree = {}
        self.root = None

    def add_node(self, val: str) -> None:
        self.tree[val] = Node(val)
        if not self.root:
            self.root = val

    def add_child(self, parent: str, child: str, wt: int) -> None:
        if parent not in self.tree:
            raise ValueError("Parent Node not present in the tree")
        self.tree[parent].add_child(child, wt)
        self.tree[child] = Node(child)

    def get_longest_path(self) -> int:
        if not self.root:
            return 0
        self.tree[self.root].update_max_paths(self)
        return self.tree[self.root].get_max_path(self)


if __name__ == "__main__":
    tree = Tree()

    tree.add_node("a")
    tree.add_child("a", "b", 3)
    tree.add_child("a", "c", 5)
    tree.add_child("a", "d", 8)
    tree.add_child("d", "e", 2)
    tree.add_child("d", "f", 4)
    tree.add_child("e", "g", 1)
    tree.add_child("e", "h", 1)

    print(tree.get_longest_path())


"""
SPECS:

TIME COMPLEXITY: O(n ^ n)
SPACE COMPLEXITY: O(n)
"""
