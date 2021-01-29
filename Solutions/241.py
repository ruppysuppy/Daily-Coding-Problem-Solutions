"""
Problem:

In academia, the h-index is a metric used to calculate the impact of a researcher's
papers. It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. If there
are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are
[4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3 papers with at
least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
"""


from typing import List


def get_h_index(citations: List[int]) -> int:
    citations.sort(reverse=True)
    for index, citation in enumerate(citations):
        if index >= citation:
            # implies that there are 'index' papers with atleast 'citation' citations
            return index
    return 0


if __name__ == "__main__":
    print(get_h_index([4, 3, 0, 1, 5]))
    print(get_h_index([4, 1, 0, 1, 1]))
    print(get_h_index([4, 4, 4, 5, 4]))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(1)
"""
