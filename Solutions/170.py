"""
Problem:

Given a start word, an end word, and a dictionary of valid words, find the shortest
transformation sequence from start to end such that only one letter is changed at each
step of the sequence, and each transformed word exists in the dictionary. If there is
no possible transformation, return null. Each word in the dictionary have the same
length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and
dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return
null as there is no possible transformation from dog to cat.
"""

from sys import maxsize
from typing import List, Optional

from DataStructures.Graph import GraphUndirectedUnweighted
from DataStructures.Queue import Queue


def is_str_different_by_1_character(s1: str, s2: str) -> bool:
    len1 = len(s1)
    len2 = len(s2)
    no_mismatch = True
    if len1 != len2:
        if abs(len1 - len2) > 1:
            return False
        no_mismatch = False

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if no_mismatch:
                no_mismatch = False
            else:
                return False
    return True


def create_graph(vert_list: List[str]) -> GraphUndirectedUnweighted:
    graph = GraphUndirectedUnweighted()
    length = len(vert_list)
    for i in range(length):
        for j in range(i, length):
            if is_str_different_by_1_character(vert_list[i], vert_list[j]):
                graph.add_edge(vert_list[i], vert_list[j])
    return graph


def bfs_path(graph: GraphUndirectedUnweighted, start: str, stop: str) -> List[str]:
    parent_map = {node: None for node in graph.connections}
    # bfs
    queue = Queue()
    seen = set()
    queue.enqueue(start)
    seen.add(start)
    while not queue.is_empty():
        node = queue.dequeue()
        for neighbour in graph.connections[node]:
            if neighbour not in seen:
                parent_map[neighbour] = node
                queue.enqueue(neighbour)
                seen.add(neighbour)
    # generating the path
    path = [stop]
    while parent_map[path[-1]] is not None:
        path.append(parent_map[path[-1]])
        if path[-1] == start:
            break
    return reversed(path)


def min_transform(start: str, stop: str, dictionary: List[str]) -> Optional[List[str]]:
    if start not in dictionary:
        dictionary.append(start)
    if stop not in dictionary:
        return None

    graph = create_graph(dictionary)
    return bfs_path(graph, start, stop)


if __name__ == "__main__":
    print(min_transform("dog", "cat", ["dot", "dop", "dat", "cat"]))
    print(min_transform("dog", "cat", ["dot", "tod", "dat", "dar"]))


"""
SPECS:

TIME COMPLEXITY: O((n ^ 2) x len(word))
SPACE COMPLEXITY: O(n ^ 2)
"""
