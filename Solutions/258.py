"""
Problem:

In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].
"""

from DataStructures.Tree import Node, Binary_Tree


def get_boustrophedon_helper(self, level, accumulator):
    # using dfs to store a list of values by level
    if level not in accumulator:
        accumulator[level] = []
    accumulator[level].append(self.val)
    if self.left:
        self.left.get_boustrophedon_helper(level + 1, accumulator)
    if self.right:
        self.right.get_boustrophedon_helper(level + 1, accumulator)


def get_boustrophedon(self):
    if not self.root:
        return []
    # generating the nodes by level
    level_data = {}
    self.root.get_boustrophedon_helper(1, level_data)
    result = []
    # adding the even levels in reverse order in the result
    for level in sorted(list(level_data.keys())):
        if level % 2 == 0:
            result.extend(reversed(level_data[level]))
        else:
            result.extend(level_data[level])
    return result


setattr(Node, "get_boustrophedon_helper", get_boustrophedon_helper)
setattr(Binary_Tree, "get_boustrophedon", get_boustrophedon)


# DRIVER CODE
tree = Binary_Tree()

tree.root = Node(1)

tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.get_boustrophedon())
