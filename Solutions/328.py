"""
Problem:

In chess, the Elo rating system is used to calculate player strengths based on game
results.

A simplified description of the Elo system is as follows. Every player begins at the
same score. For each subsequent game, the loser transfers some points to the winner,
where the amount of points transferred depends on how unlikely the win is. For example,
a 1200-ranked player should gain much more points for beating a 2000-ranked player than
for beating a 1300-ranked player.

Implement this system.
"""

from typing import Optional


class EloRating:
    INITIAL_POINTS = 1400
    MEAN_SCORE_CHANGE = 30

    def __init__(self) -> None:
        self.scores = {}

    def add_player(self, id: int) -> None:
        self.scores[id] = EloRating.INITIAL_POINTS

    def update_points(
        self, p1_id: int, p2_id: int, winner: Optional[int] = None
    ) -> None:
        if p1_id not in self.scores or p2_id not in self.scores:
            raise ValueError("Player not found")
        if winner is None:
            return
        temp = set([p1_id, p2_id]) - set([winner])
        if len(temp) != 1:
            raise ValueError("Invalid player & winner combination")
        # updating points
        loser = temp.pop()
        if self.scores[loser] > 0:
            ratio = self.scores[loser] / self.scores[winner]
            # lock to ensure there is no negative points
            points = min(self.scores[loser], int(ratio * EloRating.MEAN_SCORE_CHANGE))
            self.scores[winner] += points
            self.scores[loser] -= points

    def display_points(self) -> None:
        print("\n" + "=" * 15)
        print("POINTS")
        print("=" * 15)
        for player in self.scores:
            print(f"{player}\t{self.scores[player]}")
        print("=" * 15)


if __name__ == "__main__":
    elo = EloRating()

    elo.add_player(1)
    elo.add_player(2)
    elo.add_player(3)

    elo.display_points()

    elo.update_points(1, 2, 1)
    elo.update_points(1, 3, 1)

    elo.display_points()

    elo.update_points(1, 2, 1)

    elo.display_points()

    elo.update_points(3, 2, 3)

    elo.display_points()

    elo.update_points(3, 2)  # TIE

    elo.display_points()
