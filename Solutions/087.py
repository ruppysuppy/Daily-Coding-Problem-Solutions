"""
Problem:

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.
"""

from __future__ import annotations
from typing import Union

OPPOSITES_CARDINALS = {"N": "S", "S": "N", "E": "W", "W": "E"}


class Node:
    def __init__(self, val: str) -> None:
        self.val = val
        self.neighbours = {"N": set(), "E": set(), "S": set(), "W": set()}

    def __repr__(self) -> str:
        return f"{self.val}"

    def __eq__(self, other: Union[Node, str]) -> bool:
        if type(other) == Node:
            return self.val == other.val
        elif type(other) == str:
            return self.val == other
        return False

    def __hash__(self) -> int:
        return hash(self.val)


class Map:
    def __init__(self) -> None:
        self.nodes = {}

    def add_rule(self, rule: str) -> None:
        node1, direction, node2 = rule.split()
        node1 = Node(node1)
        node2 = Node(node2)
        # cheking for the existance of the nodes
        if node1 not in self.nodes:
            self.nodes[node1.val] = node1
        else:
            node1 = self.nodes[node1.val]
        if node2 not in self.nodes:
            self.nodes[node2.val] = node2
        else:
            node2 = self.nodes[node2.val]
        # updating the neighbours
        for char in direction:
            if (node1 in node2.neighbours[char]) or (
                node2 in node1.neighbours[OPPOSITES_CARDINALS[char]]
            ):
                raise RuntimeError
            for node in node1.neighbours[char]:
                self.add_rule(f"{node} {char} {node2}")
        # adding the rule to the calling node
        for char in direction:
            node2.neighbours[char].add(node1)
            node1.neighbours[OPPOSITES_CARDINALS[char]].add(node2)


if __name__ == "__main__":
    m = Map()

    m.add_rule("A N B")
    print("Rule Applied!")
    m.add_rule("B NE C")
    print("Rule Applied!")

    try:
        m.add_rule("C N A")
    except RuntimeError:
        print("Invalid Rule!")
