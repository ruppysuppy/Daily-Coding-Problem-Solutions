"""
Problem:

An 8-puzzle is a game played on a 3 x 3 board of tiles, with the ninth tile missing.
The remaining tiles are labeled 1 through 8 but shuffled randomly. Tiles may slide
horizontally or vertically into an empty space, but may not be removed from the board.

Design a class to represent the board, and find a series of steps to bring the board
to the state [[1, 2, 3], [4, 5, 6], [7, 8, None]].
"""

# SOLUTION FROM: https://gist.github.com/flatline/838202 (MODIFIED AND OPTIMIZED)

from math import sqrt

FINAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


def index(item, seq):
    """
    Helper function that returns -1 for non-found index value of a seq
    """
    if item in seq:
        return seq.index(item)
    else:
        return -1


class EightPuzzle:
    def __init__(self, board):
        # heuristic value
        self._hval = 0
        # search depth of current instance
        self._depth = 0
        # parent node in search path
        self._parent = None
        self.adj_matrix = []
        self.adj_matrix = board

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        else:
            return self.adj_matrix == other.adj_matrix

    def __str__(self):
        res = ""
        for row in range(3):
            res += " ".join(map(str, self.adj_matrix[row]))
            res += "\r\n"
        return res

    def _clone(self):
        copy = [[elem for elem in row] for row in self.adj_matrix]
        p = EightPuzzle(copy)
        return p

    def _get_legal_moves(self):
        """
        Returns list of tuples with which the free space may be swapped
        """
        # get row and column of the empty piece
        row, col = self.find(0)
        free = []
        # find which pieces can move there
        if row > 0:
            free.append((row - 1, col))
        if col > 0:
            free.append((row, col - 1))
        if row < 2:
            free.append((row + 1, col))
        if col < 2:
            free.append((row, col + 1))

        return free

    def _generate_moves(self):
        free = self._get_legal_moves()
        zero = self.find(0)

        def swap_and_clone(a, b):
            p = self._clone()
            p.swap(a, b)
            p._depth = self._depth + 1
            p._parent = self
            return p

        return map(lambda pair: swap_and_clone(zero, pair), free)

    def _generate_solution_path(self, path):
        if self._parent == None:
            return path
        else:
            path.append(self)
            return self._parent._generate_solution_path(path)

    def solve(self, h):
        """
        Performs A* search for goal state.
        h(puzzle) - heuristic function, returns an integer
        """

        def is_solved(puzzle):
            return puzzle.adj_matrix == FINAL_STATE

        openl = [self]
        closedl = []
        move_count = 0
        while len(openl) > 0:
            x = openl.pop(0)
            move_count += 1
            if is_solved(x):
                if len(closedl) > 0:
                    return x._generate_solution_path([]), move_count
                else:
                    return [x]

            succ = x._generate_moves()
            idx_open = idx_closed = -1
            for move in succ:
                # have we already seen this node?
                idx_open = index(move, openl)
                idx_closed = index(move, closedl)
                hval = h(move)
                fval = hval + move._depth

                if idx_closed == -1 and idx_open == -1:
                    move._hval = hval
                    openl.append(move)
                elif idx_open > -1:
                    copy = openl[idx_open]
                    if fval < copy._hval + copy._depth:
                        # copy move's values over existing
                        copy._hval = hval
                        copy._parent = move._parent
                        copy._depth = move._depth
                elif idx_closed > -1:
                    copy = closedl[idx_closed]
                    if fval < copy._hval + copy._depth:
                        move._hval = hval
                        closedl.remove(copy)
                        openl.append(move)

            closedl.append(x)
            openl = sorted(openl, key=lambda p: p._hval + p._depth)
        # if finished state not found, return failure
        return [], 0

    def find(self, value):
        """
        returns the row, col coordinates of the specified value in the graph
        """
        if value < 0 or value > 8:
            raise Exception("value out of range")

        for row in range(3):
            for col in range(3):
                if self.adj_matrix[row][col] == value:
                    return row, col

    def peek(self, row, col):
        """
        returns the value at the specified row and column
        """
        return self.adj_matrix[row][col]

    def poke(self, row, col, value):
        """
        sets the value at the specified row and column
        """
        self.adj_matrix[row][col] = value

    def swap(self, pos_a, pos_b):
        """
        swaps values at the specified coordinates
        """
        temp = self.peek(*pos_a)
        self.poke(pos_a[0], pos_a[1], self.peek(*pos_b))
        self.poke(pos_b[0], pos_b[1], temp)


def heur(puzzle, item_total_calc, total_calc):
    """
    Heuristic template that provides the current and target position for each number
    and the total function.
    
    Parameters:
    puzzle - the puzzle
    item_total_calc - takes 4 parameters: current row, target row, current col, target
        col. 
        Returns int.
    total_calc - takes 1 parameter, the sum of item_total_calc over all entries, and
        returns int. 
        This is the value of the heuristic function
    """
    t = 0
    for row in range(3):
        for col in range(3):
            val = puzzle.peek(row, col) - 1
            target_col = val % 3
            target_row = val / 3
            # account for 0 as blank
            if target_row < 0:
                target_row = 2
            t += item_total_calc(row, target_row, col, target_col)
    return total_calc(t)


# some heuristic functions, the best being the standard manhattan distance in this
# case, as it comes closest to maximizing the estimated distance while still being
# admissible.


def h_manhattan(puzzle):
    return heur(puzzle, lambda r, tr, c, tc: abs(tr - r) + abs(tc - c), lambda t: t)


def h_manhattan_lsq(puzzle):
    return heur(
        puzzle,
        lambda r, tr, c, tc: (abs(tr - r) + abs(tc - c)) ** 2,
        lambda t: sqrt(t),
    )


def h_linear(puzzle):
    return heur(
        puzzle,
        lambda r, tr, c, tc: sqrt(sqrt((tr - r) ** 2 + (tc - c) ** 2)),
        lambda t: t,
    )


def h_linear_lsq(puzzle):
    return heur(
        puzzle, lambda r, tr, c, tc: (tr - r) ** 2 + (tc - c) ** 2, lambda t: sqrt(t),
    )


def solve_8_puzzle(board):
    transformed_board = [[elem if elem else 0 for elem in row] for row in board]
    p = EightPuzzle(transformed_board)
    print(p)

    path, count = p.solve(h_manhattan)
    path.reverse()
    for i in path:
        print(i)

    print("Solved with Manhattan distance exploring", count, "states")
    path, count = p.solve(h_manhattan_lsq)
    print("Solved with Manhattan least squares exploring", count, "states")
    path, count = p.solve(h_linear)
    print("Solved with linear distance exploring", count, "states")
    path, count = p.solve(h_linear_lsq)
    print("Solved with linear least squares exploring", count, "states")


if __name__ == "__main__":
    board = [
        [4, 1, 2],
        [7, 5, 3],
        [None, 8, 6]
    ]
    solve_8_puzzle(board)
