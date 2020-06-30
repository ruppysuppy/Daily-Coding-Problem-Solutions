'''
Problem:

Boggle is a game played on a 4 x 4 grid of letters. 
The goal is to find as many words as possible that can be formed by a sequence of adjacent letters in the grid, using each cell at most once. 
Given a game board and a dictionary of valid words, implement a Boggle solver.
'''

from DataStructures.Trie import Trie


def get_neighbours(pos):
    i, j = pos
    neighbours = []

    all_neighbours = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j + 1),
        (i + 1, j + 1),
        (i + 1, j),
        (i + 1, j - 1),
        (i, j - 1)
    ]

    for y, x in all_neighbours:
        if (0 <= x < 4 and 0 <= y < 4):
            neighbours.append((y, x))
    return neighbours


def get_words(matrix, pos, trie, curr, res):
    possibilities = trie.get_suggestions(curr)

    if (not possibilities):
        return
    if (len(possibilities) == 1 and list(possibilities)[0] == curr):
        res.add(curr)
        return
    
    for neighbour in get_neighbours(pos):
        i, j = neighbour
        get_words(matrix, neighbour, trie, curr+matrix[i][j], res)
    
    return


def solve_Boggle(matrix, dictionary):
    prefix_tree = Trie()
    prefix_tree.add_words(dictionary)

    res = set()

    for i in range(4):
        for j in range(4):
            if (matrix[i][j] in prefix_tree.root.children):
                get_words(matrix, (i, j), prefix_tree, matrix[i][j], res)
    
    return res


# DRIVER CODE
board = [
    ["A", "L", "B", "P"],
    ["C", "O", "E", "Y"],
    ["F", "C", "H", "O"],
    ["B", "A", "D", "A"]
]
words_in_board = {
    "PECH", "COLA", "YO", "BAD"
    }
words_not_in_board = {
    "FOR", "BULL"
}
dictionary = words_in_board | words_not_in_board

print(dictionary)
print(solve_Boggle(board, dictionary))