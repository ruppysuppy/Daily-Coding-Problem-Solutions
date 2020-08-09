"""
Problem:

You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. 
Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

Example:

Start state = 'a'
Number of steps = 5000
Transition probabilities = [
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce {'a': 3012, 'b': 1656, 'c': 332 }
"""

# imporing randint
from random import random

# graph class (directed)
class Graph:
    # initialization
    def __init__(self):
        self.nodes = {}

    # adding new node
    def add_node(self, node):
        self.nodes[node] = {}

    # adding the edges with the required probability
    def add_transition_probability(self, node1, node2, probability):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)

        self.nodes[node1][node2] = probability

    # getting the node being transitioned to
    def transition(self, node):
        transition = random()
        curr = 0

        for key in self.nodes[node]:
            curr += self.nodes[node][key]
            if curr > transition:
                return key


# FUNCTION TO PERFORM THE OPERATION
def get_transitions(start, transitions, steps):
    # initializing the graph
    graph = Graph()

    # getting the nodes
    nodes = set()

    for x, y, _ in transitions:
        nodes.add(x)
        nodes.add(y)

    # creating a visited frequency dictionary
    visited = {node: 0 for node in nodes}

    # creating the graph
    for transition in transitions:
        node1, node2, probability = transition
        graph.add_transition_probability(node1, node2, probability)

    # initializing the traversal
    node = graph.transition(start)
    visited[node] += 1

    # traversing and storing the details
    for _ in range(steps - 1):
        node = graph.transition(node)
        visited[node] += 1

    # returning the visited frequency
    return visited


# DRIVER CODE
transitions = [
    ("a", "a", 0.9),
    ("a", "b", 0.075),
    ("a", "c", 0.025),
    ("b", "a", 0.15),
    ("b", "b", 0.8),
    ("b", "c", 0.05),
    ("c", "a", 0.25),
    ("c", "b", 0.25),
    ("c", "c", 0.5),
]
print(get_transitions("a", transitions, 5000))
