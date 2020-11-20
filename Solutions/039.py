"""
Problem:

Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies. Any live cell with two or three
live neighbours remains living. Any live cell with more than three live neighbours
dies. Any dead cell with exactly three live neighbours becomes a live cell. A cell
neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting
list of live cell coordinates and the number of steps it should run for. Once
initialized, it should print out the board state at each step. Since it's an infinite
board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to
bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

from __future__ import annotations
from sys import maxsize
from typing import Any, List, Set


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: Any) -> bool:
        if type(other) != Coordinate:
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def get_neighbours(self) -> List[Coordinate]:
        return [
            Coordinate(self.x - 1, self.y),
            Coordinate(self.x - 1, self.y + 1),
            Coordinate(self.x, self.y + 1),
            Coordinate(self.x + 1, self.y + 1),
            Coordinate(self.x + 1, self.y),
            Coordinate(self.x + 1, self.y - 1),
            Coordinate(self.x, self.y - 1),
            Coordinate(self.x - 1, self.y - 1),
        ]


def show_board(alive_cells: Set[Coordinate]) -> None:
    x_max, x_min = -maxsize, maxsize
    y_max, y_min = -maxsize, maxsize
    # generating bounds
    for cell in alive_cells:
        x, y = cell.x, cell.y
        x_min, x_max = min(x_min, x), max(x_max, x)
        y_min, y_max = min(y_min, y), max(y_max, y)
    # displaying the board
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if Coordinate(x, y) in alive_cells:
                print("*", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


def play_game(board: List[Coordinate], n: int) -> None:
    alive_cells = set(board)
    print("Initail Board of Game of Life:")
    show_board(alive_cells)

    for i in range(1, n + 1):
        # alive cells cells cannot be modified inside the loop, using dead and alice
        # lists to track changes
        dead = []
        alive = []
        for cell in alive_cells:
            alive_neighbours = 0
            neighbours = cell.get_neighbours()
            for neighbour in neighbours:
                # checking how many live neighbours the cell has
                if neighbour in alive_cells:
                    alive_neighbours += 1
                # checking how many live neighbours the cell (neighbour) has
                if neighbour not in alive_cells:
                    neighbours_of_neighbour = neighbour.get_neighbours()
                    alive_neighbours_of_neighbour = 0
                    for neighbour_of_neighbour in neighbours_of_neighbour:
                        if neighbour_of_neighbour in alive_cells:
                            alive_neighbours_of_neighbour += 1
                    if alive_neighbours_of_neighbour == 3:
                        alive.append(neighbour)
            if alive_neighbours < 2 or alive_neighbours > 3:
                dead.append(cell)

        # removing dead cells
        for cell in dead:
            alive_cells.remove(cell)
        # adding new live cells
        for cell in alive:
            alive_cells.add(cell)
        # displaying board
        print(f"Iteration {i}:")
        show_board(alive_cells)


if __name__ == "__main__":
    board_0 = [Coordinate(0, 0), Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 5)]
    play_game(board_0, 3)

    board_1 = [
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(1, 1),
        Coordinate(1, 5),
        Coordinate(2, 5),
        Coordinate(2, 6),
    ]
    play_game(board_1, 4)

    board_2 = [
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(1, 1),
        Coordinate(2, 5),
        Coordinate(2, 6),
        Coordinate(3, 9),
        Coordinate(4, 8),
        Coordinate(5, 10),
    ]
    play_game(board_2, 4)


"""
SPECS:

TIME COMPLEXITY: O((alive cells ^ 2) x n)
SPACE COMPLEXITY: O(alive cells)
"""
