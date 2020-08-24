"""
Problem:

Given an integer N, construct all possible binary search trees with N nodes.
"""

from copy import deepcopy
from functools import lru_cache
from typing import List

from DataStructures.Tree import BinaryTree, Node


# memorized fibonacci function
@lru_cache(maxsize=128)
def fib(n: int) -> int:
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


# Tree generator functions
def generate_tree_helper(i: int, arr: List[BinaryTree], nodes: int) -> BinaryTree:
    tree = arr[i]
    stack = [tree.root]

    while stack:
        # generating the new tree with 1 new node
        node = stack.pop()
        if not node.left:
            node.left = Node(0)
            for j in range(nodes):
                if j != i and tree == arr[j]:
                    node.left = None
                    break
            else:
                return tree
        else:
            stack.append(node.left)
        if not node.right:
            node.right = Node(0)
            for j in range(nodes):
                if j != i and tree == arr[j]:
                    node.right = None
                    break
            else:
                return tree
        else:
            stack.append(node.right)


def generate_tree(tree: BinaryTree) -> List[BinaryTree]:
    # generating a list of trees to update with a new node and calling the helper
    # function
    nodes = sum([fib(i) for i in range(1, len(tree) + 2)])
    arr = [deepcopy(tree) for _ in range(nodes)]
    for i in range(nodes):
        arr[i] = generate_tree_helper(i, arr, nodes)
    return arr


# Tree generation initialization
def create_trees_helper(tree_arr: List[BinaryTree], n: int) -> None:
    if n == 0:
        return
    new_tree_arr = []
    for tree in tree_arr:
        result = generate_tree(tree)
        new_tree_arr.extend(
            [temp for temp in result if temp and temp not in new_tree_arr]
        )  # can be optimized by using a set and overloading __hash__ in tree class
    tree_arr[:] = new_tree_arr
    create_trees_helper(tree_arr, n - 1)


def create_trees(n: int) -> List[BinaryTree]:
    # function to create all binary trees containing n nodes
    tree_arr = []
    if n == 0:
        return tree_arr
    tree = BinaryTree()
    tree.root = Node(0)
    tree_arr.append(tree)
    create_trees_helper(tree_arr, n - 1)
    return tree_arr


if __name__ == "__main__":
    for tree in create_trees(2):
        print(tree)
    print()
    for tree in create_trees(3):
        print(tree)
    print()
