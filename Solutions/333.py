"""
Problem:

At a party, there is a single person who everyone knows, but who does not know anyone
in return (the "celebrity"). To help figure out who this is, you have access to an O(1)
method called knows(a, b), which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity
in O(N) time.
"""

from typing import Dict, Set


class Party:
    def __init__(self, people: Dict[str, Set[str]]) -> None:
        self.people = people

    def knows(self, a: str, b: str) -> bool:
        # function to check if a knows b [runs in O(1)]
        return b in self.people[a]

    def get_celebrity(self) -> str:
        # runs in O(v + e) time & space (e = the maximum people a person knows,
        # v = number of people)
        celebrity_candidates = {}
        for person in self.people:
            if celebrity_candidates == {}:
                # getting potential celebrities if the celebrity candidates is empty
                # the values are filled with people the 1st person knows who doesn't
                # know him (celebrity candidates will contain all popular people
                # including the celebrity)
                for person2 in self.people[person]:
                    if not self.knows(person2, person):
                        celebrity_candidates[person2] = 1
                continue
            # checking for the person known by most people in case there is other
            # popular people
            for potential_celebrity in celebrity_candidates:
                if potential_celebrity in self.people[person]:
                    celebrity_candidates[potential_celebrity] += 1
        return max(
            celebrity_candidates.keys(),
            key=lambda candidate: celebrity_candidates[candidate],
        )


if __name__ == "__main__":
    people = {
        "a": {"b"},  # popular person (but not the celebrity)
        "b": set(),  # celebrity
        "c": {"a", "b", "d"},
        "d": {"a", "b"},
    }
    party = Party(people)
    print(party.get_celebrity())
