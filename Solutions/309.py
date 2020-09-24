"""
Problem:

There are M people sitting in a row of N seats, where M < N. Your task is to
redistribute people such that there are no gaps between any of them, while keeping
overall movement to a minimum.

For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1], where
0 represents an empty seat and 1 represents a person. In this case, one solution would
be to place the person on the right in the fourth seat. We can consider the cost of a
solution to be the sum of the absolute distance each person must move, so that the cost
here would be 5.

Given an input such as the one above, return the lowest possible cost of moving people
to remove all gaps.
"""

from itertools import permutations
from sys import maxsize
from typing import List, Set


def get_people_indices(arr: List[int]) -> Set[int]:
    return set([index for index, occupied in enumerate(arr) if occupied])


def get_min_dist(vacant_spots: List[int], available_people: List[int]) -> int:
    # generating all permutations and returning the minumum cost
    min_dist = maxsize
    length = len(vacant_spots)
    permutation_list = list(permutations(range(length)))
    for permutation in permutation_list:
        dist = 0
        for i in range(length):
            k = permutation[i]
            dist += abs(vacant_spots[i] - available_people[k])
        min_dist = min(min_dist, dist)
    return min_dist


def get_lowest_cost(arr: List[int]) -> int:
    num_people = sum(arr)
    if num_people in (0, 1):
        return 0
    starting_people_indices = get_people_indices(arr)
    lowest_cost = maxsize
    # generating all possible valid seating arrangements and getting the minimum cost
    for offset in range(len(arr) - num_people + 1):
        subarr = arr[offset : offset + num_people]
        all_indices = set([offset + x for x in range(num_people)])
        people_indices = set([offset + x for x in get_people_indices(subarr)])

        vacant_indices = list(all_indices - people_indices)
        occupied_indices = list(starting_people_indices - people_indices)
        lowest_cost = min(lowest_cost, get_min_dist(vacant_indices, occupied_indices))
    return lowest_cost


if __name__ == "__main__":
    print(get_lowest_cost([0, 1, 1, 0, 1, 0, 0, 0, 1]))
    print(get_lowest_cost([0, 1, 0, 0, 1, 0, 1, 0, 1]))
    print(get_lowest_cost([1, 1, 0, 0, 1, 0, 1, 0, 1]))
    print(get_lowest_cost([1, 1, 1, 1, 1, 0, 0, 0, 0]))


"""
SPECS:

TIME COMPLEXITY: O(n x n!)
SPACE COMPLEXITY: O(n!)
"""
