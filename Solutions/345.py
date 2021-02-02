"""
Problem:

You are given a set of synonyms, such as (big, large) and (eat, consume). Using this
set, determine if two sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:

"He wants to eat food."
"He wants to consume food."
Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c): consider the
case of (coach, bus) and (coach, teacher).

Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply (b, c)?
"""

from typing import List, Tuple, Union

from DataStructures.Graph import GraphUndirectedUnweighted


def generate_graph(synonyms: List[Tuple[str, str]]) -> GraphUndirectedUnweighted:
    graph = GraphUndirectedUnweighted()
    for word_1, word_2 in synonyms:
        graph.add_edge(word_1, word_2)
    return graph


def check_equivalence(
    sentence_1: str, sentence_2: str, synonyms: List[Tuple[str, str]]
) -> bool:
    graph = generate_graph(synonyms)
    word_list_1 = sentence_1.strip().split()
    word_list_2 = [word for word in word_list_1]

    if len(word_list_1) != len(word_list_2):
        return False
    for word_1, word_2 in zip(word_list_1, word_list_2):
        if word_1 != word_2:
            if word_1 not in graph.connections or word_2 not in graph.connections:
                return False
            if word_2 not in graph.connections[word_1]:
                return False
    return True


if __name__ == "__main__":
    print(
        check_equivalence(
            "He wants to eat food.", "He wants to consume food.", [("eat", "consume")]
        )
    )
    print(
        check_equivalence(
            "He is waiting for the bus.",
            "He is waiting for the teacher.",
            [("coach", "bus"), ("coach", "teacher")],
        )
    )

# if we can assume that (a, b) and (a, c) do in fact imply (b, c), then for each word,
# we would have to run a dfs/bfs to get all words similar to any given word, instead of
# simply comparing: 'word_2 not in graph.connections[word_1]'


"""
SPECS:

TIME COMPLEXITY: O(characters)
SPACE COMPLEXITY: O(words ^ 2)
"""
