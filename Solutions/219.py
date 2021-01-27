"""
Problem:

Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6
vertically suspended grid. The game ends either when one player creates a line of four
consecutive discs of their color (horizontally, vertically, or diagonally), or when
there are no more spots left in the grid.

Design and implement Connect 4.
"""

from typing import Optional


class Connect4:
    def __init__(self) -> None:
        self.board = [["-" for _ in range(7)] for _ in range(6)]
        self.to_play = "R"

    def get_empty(self, position: int) -> int:
        if self.board[0][position] != "-":
            return -1
        if self.board[5][position] == "-":
            return 5

        for i in range(5):
            if self.board[i][position] == "-" and self.board[i + 1][position] != "-":
                return i

    def play_turn(self) -> None:
        position = int(input("Enter the location to put the disk: "))
        position -= 1
        row = self.get_empty(position)

        while row == -1:
            position = int(input("Enter the location to put the disk: "))
            position -= 1
            row = self.get_empty(position)

        if self.to_play == "R":
            self.board[row][position] = "R"
            self.to_play = "B"
        else:
            self.board[row][position] = "B"
            self.to_play = "R"

    def victory_check(self) -> Optional[str]:
        # horizontal check
        for i in range(6):
            for j in range(4):
                if self.board[i][j] in ("R", "B"):
                    disk = self.board[i][j]
                    for k in range(j, j + 4):
                        if self.board[i][k] != disk:
                            break
                    else:
                        return disk
        # vertical check
        for i in range(3):
            for j in range(7):
                if self.board[i][j] in ("R", "B"):
                    disk = self.board[i][j]
                    for k in range(i, i + 4):
                        if self.board[k][j] != disk:
                            break
                    else:
                        return disk
        # top left to bottom right diagonal check
        for i in range(2):
            for j in range(3):
                if self.board[i][j] in ("R", "B"):
                    disk = self.board[i][j]
                    for k in range(4):
                        if self.board[i + k][j + k] != disk:
                            break
                    else:
                        return disk
        # top right to bottom left diagonal check
        for i in range(3, 6):
            for j in range(4, 7):
                if self.board[i][j] in ("R", "B"):
                    disk = self.board[i][j]
                    for k in range(4):
                        if self.board[i - k][j - k] != disk:
                            break
                    else:
                        return disk
        return None

    def full_check(self) -> bool:
        for i in range(6):
            for j in range(7):
                if self.board[i][j] == "-":
                    return False
        return True

    def print_board(self) -> None:
        for i in range(6):
            for j in range(7):
                print(self.board[i][j], end=" ")
            print()

    def play(self) -> None:
        while not self.full_check() and not self.victory_check():
            try:
                print(self.to_play, "to play")
                self.play_turn()
                print("Board: ")
                self.print_board()
                print()
            except IndexError:
                print("Illegal move!")

        if self.full_check():
            print("Its a draw")
        else:
            print("{} has won".format(self.victory_check()))


if __name__ == "__main__":
    Connect4().play()
