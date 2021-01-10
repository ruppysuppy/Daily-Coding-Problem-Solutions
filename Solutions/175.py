"""
Problem:

You are given a starting state start, a list of transition probabilities for a Markov
chain, and a number of steps num_steps. Run the Markov chain starting from start for
num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following
transition probabilities:

[
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

One instance of running this Markov chain might produce
{'a': 3012, 'b': 1656, 'c': 332 }.
"""

from random import random
from typing import Dict, List, Tuple

from DataStructures.Graph import GraphDirectedWeighted


def get_transition_form_node(graph: GraphDirectedWeighted, node: str) -> str:
    transition = random()
    curr = 0
    for neighbour in graph.connections[node]:
        curr += graph.connections[node][neighbour]
        if curr >= transition:
            return neighbour


def get_transitions(
    start: str, transitions: List[Tuple[str, str, float]], steps: int
) -> Dict[str, int]:
    # generating graph
    graph = GraphDirectedWeighted()
    for (node1, node2, probability) in transitions:
        graph.add_edge(node1, node2, probability)
    # generating visited map
    visited = {node: 0 for node in graph.connections}
    node = start
    for _ in range(steps):
        node = get_transition_form_node(graph, node)
        visited[node] += 1
    return visited


if __name__ == "__main__":
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


"""
SPECS:

TIME COMPLEXITY: O(steps + transition states)
SPACE COMPLEXITY: O(transition states)
"""
