# NOTE: The code is a bit messy as I finished it in a rush

"""
Problem:

Conway's Game of Life takes place on an infinite two-dimensional board of square cells.

Each cell is either dead or alive, and at each tick, the following rules apply:
* Any live cell with less than two live neighbours dies.
* Any live cell with two or three live neighbours remains living.
* Any live cell with more than three live neighbours dies.
* Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent

Implement Conway's Game of Life. 
It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. 
Once initialized, it should print out the board state at each step. 
Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.
You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

# Coordinate Object
class Coordinate:
    # Initialization function
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinate = (x, y)

    # String function
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Representation function
    def __repr__(self):
        return self.__str__()

    # Function to return all the neighbours in x-y plane
    def get_neighbours(self):
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


# Function to display the board
def show_board(alive_cells):
    # Variables to store the minimum and maximum x and y coordinates
    x_max = -9999
    x_min = 9999
    y_max = -9999
    y_min = 9999

    # Getting the actual value for x_max, x_min, y_max and y_min
    for cell in alive_cells:
        if cell[0] > x_max:
            x_max = cell[0]
        if cell[0] < x_min:
            x_min = cell[0]
        if cell[1] > y_max:
            y_max = cell[1]
        if cell[1] < y_min:
            y_min = cell[1]

    # Printing the state of the board (in the region under consideration - live cells present)
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if (x, y) in alive_cells:
                print("*", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


# FUNCTION TO PERFORM THE OPERATION
def play_game(board, n):
    # Alive cells is a set of tuples having the coordinates of the live cells
    alive_cells = set([cell.coordinate for cell in board])
    print("Initail Board of Game of Life:")
    show_board(alive_cells)

    # Running the game for n iterations
    for i in range(1, n + 1):
        # dead stores the coordinates of the cells which die in the current iterations
        # alive stores the coordinates of the cells which come alive in the current iterations
        dead = []
        alive = []

        # Looping over the alive cells
        for cell in alive_cells:
            # alive neighbours contains the number of alive neighbours of a cell
            alive_neighbours = 0
            # list of all neighbours
            neighbours = [
                cell_neighbour.coordinate
                for cell_neighbour in Coordinate(cell[0], cell[1]).get_neighbours()
            ]

            # checking how many neighbours the cell has
            for neighbour in neighbours:
                if neighbour in alive_cells:
                    alive_neighbours += 1

            # if the cell is supposed to die, adding to the dead list (as cannot change alive cells in runtime)
            if alive_neighbours < 2 or alive_neighbours > 3:
                dead.append(cell)

        # Removing dead cells
        for cell in dead:
            alive_cells.remove(cell)

        # Looping over the alive cells
        for cell in alive_cells:
            # list of all neighbours
            neighbours = [
                cell_neighbour.coordinate
                for cell_neighbour in Coordinate(cell[0], cell[1]).get_neighbours()
            ]

            # Looping over the dead cells with live neighbours
            for neighbour in neighbours:
                if neighbour not in alive_cells:
                    # list of all neighbours of dead cells with live neighbours
                    neighbour_neighbours = [
                        cell_neighbour.coordinate
                        for cell_neighbour in Coordinate(
                            neighbour[0], neighbour[1]
                        ).get_neighbours()
                    ]
                    alive_neighbours = 0

                    # Getting the number of live neighbours
                    for neighbour_neighbour in neighbour_neighbours:
                        if neighbour_neighbour in alive_cells:
                            alive_neighbours += 1

                    # if the cell is supposed to come alive, adding to the alive list (as cannot change alive cells in runtime)
                    if alive_neighbours == 3:
                        alive.append(neighbour)

        # Adding new live cells
        for cell in alive:
            alive_cells.add(cell)

        # Displaying results
        print(f"Iteration {i}:")
        show_board(alive_cells)


# DRIVER CODE
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
