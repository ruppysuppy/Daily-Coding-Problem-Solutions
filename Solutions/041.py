"""
Problem:

Given an unordered list of flights taken by someone, each represented as
(origin, destination) pairs, and a starting airport, compute the person's itinerary. If
no such itinerary exists, return null. If there are multiple possible itineraries,
return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights
[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport
'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM',
you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting
airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though
['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is
lexicographically smaller.
"""

from typing import List, Optional, Tuple


def get_itinerary(
    flights: List[Tuple[str, str]],
    current_position: str,
    current_itinerary: List[str] = [],
) -> Optional[List[str]]:
    if not flights and current_itinerary:
        return current_itinerary + [current_position]
    elif not flights:
        return None

    resulatant_itinerary = None
    # generating the itinerary
    for index, (src, dest) in enumerate(flights):
        # the is constructed using the current position (using DFS)
        if current_position == src:
            child_itinerary = get_itinerary(
                flights[:index] + flights[index + 1 :], dest, current_itinerary + [src]
            )
            if child_itinerary and (
                not resulatant_itinerary or child_itinerary < resulatant_itinerary
            ):
                resulatant_itinerary = child_itinerary
    return resulatant_itinerary


if __name__ == "__main__":
    print(
        get_itinerary(
            [("SFO", "HKO"), ("YYZ", "SFO"), ("YUL", "YYZ"), ("HKO", "ORD")], "YUL"
        )
    )
    print(get_itinerary([("SFO", "COM"), ("COM", "YYZ")], "COM"))
    print(get_itinerary([("A", "B"), ("A", "C"), ("B", "C"), ("C", "A")], "A"))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 3)
SPACE COMPLEXITY: O(n ^ 2)
"""
