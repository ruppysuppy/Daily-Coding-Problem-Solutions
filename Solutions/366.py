""" 
This function uses a set to keep track of all pairs of players that have played against each other. For each round of games, it separates the players into two teams, and then adds all pairs of players from the different teams to the set. At the end, it checks that all possible pairs of players have been added to the set, and if not, it returns False. Otherwise, it returns True.

This implementation should have a time complexity of O(nm^2) because we are iterating through all m rounds, n players in each round, and also n^2 pairs of players in the final check.
"""


def solutions(n: int, m: int, games) -> bool:
    played = set()
    for i in range(m):
        team1 = set(games[i][:n//2])
        team2 = set(games[i][n//2:])
        for player1 in team1:
            for player2 in team2:
                played.add((player1, player2))
                played.add((player2, player1))
    for x in range(1, n+1):
        for y in range(x+1, n+1):
            if (x, y) not in played:
                return False
    return True


if __name__ == "main ":
    n = int(input())
    m = int(input())
    mtx = [[int(val) for val in pair.split()]
           for pair in input().strip().split(', ')]
    output = solutions(n, m, mtx)
    if output == True:
        print("true")
    else:
        print("false")
