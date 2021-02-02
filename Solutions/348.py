"""
Problem:

A ternary search tree is a trie-like data structure where each node may have up to
three children. Here is an example which represents the words code, cob, be, ax, war
and we.

       c
    /  |  \
   b   o   w
 / |   |   |
a  e   d   a
|    / |   | \ 
x   b  e   r  e
The tree is structured according to the following rules:

left child nodes link to words lexicographically earlier than the parent prefix
right child nodes link to words lexicographically later than the parent prefix
middle child nodes continue the current word
For instance, since code is the first word inserted in the tree, and cob
lexicographically precedes cod, cob is represented as a left child extending from cod.

Implement insertion and search functions for a ternary search tree.
"""

from random import shuffle, random
from typing import Optional


class Node:
    def __init__(self, val: Optional[str] = None) -> None:
        self.val = val
        self.left = None
        self.mid = None
        self.right = None

    def __bool__(self) -> bool:
        return bool(self.val)

    def insert_helper(self, string: str) -> None:
        if not string:
            return

        if self.left is None:
            self.left = Node()
        if self.mid is None:
            self.mid = Node()
        if self.right is None:
            self.right = Node()

        char = string[0]
        if not self:
            self.val = char
            self.mid.insert_helper(string[1:])
        if self.val == char:
            self.mid.insert_helper(string[1:])
        elif self.val > char:
            self.left.insert_helper(string)
        else:
            self.right.insert_helper(string)

    def search_helper(self, string: str) -> bool:
        if not string:
            return True

        char = string[0]
        length = len(string)
        if char == self.val:
            if self.mid:
                return self.mid.search_helper(string[1:])
            elif length == 1:
                return True
            return False
        elif char < self.val:
            if self.left:
                return self.left.search_helper(string)
            return False
        else:
            if self.right:
                return self.right.search_helper(string)
            return False


class TernarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, string: str) -> None:
        if not string:
            return
        if not self.root:
            self.root = Node(string[0])
            string = string[1:]
            curr = self.root
            for char in string:
                curr.mid = Node(char)
                curr = curr.mid
        else:
            self.root.insert_helper(string)

    def search(self, string: str) -> bool:
        if not string:
            return True
        if not self.root:
            return False
        return self.root.search_helper(string)


if __name__ == "__main__":
    words_present = ["ax", "be", "cob", "code", "war", "we"]
    words_absent = ["axe", "bee", "creed", "hi", "see", "wax"]

    chosen_words = words_absent + words_present
    shuffle(chosen_words)
    chosen_words = [word for word in chosen_words if random() > 0.5]
    shuffle(chosen_words)

    tree = TernarySearchTree()

    for word in words_present:
        tree.insert(word)

    for word in chosen_words:
        if tree.search(word):
            print(f"'{word}' is PRESENT in the tree")
        else:
            print(f"'{word}' is NOT PRESENT in the tree")
