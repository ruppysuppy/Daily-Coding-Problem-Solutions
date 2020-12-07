"""
Problem:

On election day, a voting machine writes data in the form (voter_id, candidate_id) to a
text file. Write a program that reads this file as a stream and returns the top 3
candidates at any given time. If you find a voter voting more than once, report this as
fraud.
"""

from typing import List


class MultipleVoteError(Exception):
    pass


class VotingMachine:
    def __init__(self, filename: str = "data.txt") -> None:
        with open(filename, "r") as f:
            lines = f.readlines()
        self.data = [line.rstrip("\n").split(",") for line in lines]

    def get_top_3(self) -> List[str]:
        # runs in O(n) time and space
        voters = set()
        votes = {}
        # calculating votes
        for voter, candidate in self.data:
            if voter in voters:
                raise MultipleVoteError(f"Voter {voter} has voted multiple times")
            voters.add(voter)
            if candidate not in votes:
                votes[candidate] = 0
            votes[candidate] += 1
        # geneating the top 3 participants
        candidates = list(votes.items())
        candidates.sort(reverse=True, key=lambda x: x[1])
        return [candidate for candidate, _ in candidates[:3]]


if __name__ == "__main__":
    print("Data Set 1:")
    vm = VotingMachine()
    print(vm.get_top_3())

    print("\nData Set 2:")
    try:
        vm = VotingMachine("dataError.txt")
        vm.get_top_3()
    except MultipleVoteError as E:
        print(E)
