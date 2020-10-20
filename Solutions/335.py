"""
Problem:

PageRank is an algorithm used by Google to rank the importance of different websites.
While there have been changes over the years, the central idea is to assign each site
a score based on the importance of other pages that link to that page.

More mathematically, suppose there are N sites, and each site i has a certain count Ci
of outgoing links. Then the score for a particular site Sj is defined as :

score(Sj) = (1 - d) / N + d * (score(Sx) / Cx+ score(Sy) / Cy+ ... + score(Sz) / Cz))
Here, Sx, Sy, ..., Sz denote the scores of all the other sites that have outgoing links
to Sj, and d is a damping factor, usually set to around 0.85, used to model the
probability that a user will stop searching.

Given a directed graph of links between various websites, write a program that
calculates each site's page rank.
"""

from typing import Dict, List, Union

from DataStructures.Graph import GraphDirectedUnweighted

DAMPING_FACTOR = 0.85


def calculate_score(
    node: Union[int, str],
    graph: GraphDirectedUnweighted,
    page_scores: Dict[Union[int, str], float],
) -> float:
    # caclulate the page score of the given page
    aggregate_score = 0
    for other in graph.connections:
        if node in graph.connections[other]:
            if page_scores[other] is None:
                # considering there is no cyclic dependency
                page_scores[other] = calculate_score(other, graph, page_scores)
            aggregate_score += page_scores[other] / len(graph.connections[other])
    score = ((1 - DAMPING_FACTOR) / len(graph)) + (DAMPING_FACTOR * aggregate_score)
    return round(score, 2)


def get_page_rank(graph: GraphDirectedUnweighted) -> List[Union[int, str]]:
    page_scores = {node: None for node in graph.connections}
    for node in graph.connections:
        page_scores[node] = calculate_score(node, graph, page_scores)
    # returning the pages sorted in the reverse order of their page scores
    return sorted(
        [page for page in page_scores],
        key=lambda page: page_scores[page],
        reverse=True,
    )


if __name__ == "__main__":
    graph = GraphDirectedUnweighted()

    graph.add_edge("a", "b")
    graph.add_edge("a", "c")

    graph.add_edge("b", "c")

    graph.add_edge("d", "a")
    graph.add_edge("d", "b")
    graph.add_edge("d", "c")

    print(get_page_rank(graph))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
