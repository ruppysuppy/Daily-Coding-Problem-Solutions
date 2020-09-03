"""
Problem:

You are given a list of (website, user) pairs that represent users visiting websites.
Come up with a program that identifies the top k pairs of websites with the greatest
similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
Then a reasonable similarity metric would most likely conclude that a and e are the
most similar, so your program should return [('a', 'e')].
"""

from typing import Dict, List, Set, Tuple


def get_similarity_score(
    visited_map: Dict[str, Set[int]], site1: str, site2: str
) -> float:
    union = visited_map[site1] | visited_map[site2]
    intersection = visited_map[site1] & visited_map[site2]
    return len(intersection) / len(union)


def create_visit_map(visited_websites: List[Tuple[str, int]]) -> Dict[str, Set[int]]:
    visited_map = {}
    for site, user in visited_websites:
        if site not in visited_map:
            visited_map[site] = set()
        visited_map[site].add(user)
    return visited_map


def get_similar_websites_helper(
    visited_websites: List[Tuple[str, int]]
) -> Dict[str, Dict[str, float]]:
    similarity = {}
    visited_map = create_visit_map(visited_websites)
    for site1 in visited_map:
        for site2 in visited_map:
            if site1 not in similarity:
                similarity[site1] = {}
            if site2 not in similarity:
                similarity[site2] = {}
            if site1 != site2 and site2 not in similarity[site1]:
                similarity_score = get_similarity_score(visited_map, site1, site2)
                similarity[site1][site2] = similarity_score
                similarity[site2][site1] = similarity_score
    return similarity


def get_similar_websites(
    visited_websites: List[Tuple[str, int]], k: int
) -> List[Tuple[str, str]]:
    similarity_map = get_similar_websites_helper(visited_websites)
    # generating the similar sites array
    arr = [
        (site1, site2, similarity_map[site1][site2])
        for site2 in similarity_map
        for site1 in similarity_map
        if site1 != site2
    ]
    arr.sort(reverse=True, key=lambda x: x[2])
    # generating the top k similar websites
    result = []
    for i in range(k):
        # choosing every 2nd element as every 2 consecutive elements are the equivalent
        # ("a", "b") is equivalent to ("b", "a")
        site1, site2, _ = arr[2 * i]
        result.append((site1, site2))
    return result


if __name__ == "__main__":
    visited_websites = [
        ("a", 1),
        ("a", 3),
        ("a", 5),
        ("b", 2),
        ("b", 6),
        ("c", 1),
        ("c", 2),
        ("c", 3),
        ("c", 4),
        ("c", 5),
        ("d", 4),
        ("d", 5),
        ("d", 6),
        ("d", 7),
        ("e", 1),
        ("e", 3),
        ("e", 5),
        ("e", 6),
    ]
    print(get_similar_websites(visited_websites, 1))
    print(get_similar_websites(visited_websites, 3))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
