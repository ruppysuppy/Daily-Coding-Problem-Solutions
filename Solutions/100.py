'''
Problem:

You are in an infinite 2D grid where you can move in any of the 8 directions:
(x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input = [(0, 0), (1, 1), (1, 2)] 
Output = 2 (It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2))
'''

# FUNCTION TO PERFORM THE OPERATION
def get_min_steps(sequence):
    # getting the length of the sequence
    length = len(sequence)

    # returning 0 if there is 1 or no element
    if (length in [0, 1]):
        return 0
    
    # getting the current position
    curr = sequence[0]
    # storing the total distance covered
    dist = 0

    # looping over the sequence from the 1st element
    for next_pos in sequence[1:]:
        # breaking the current position into i and j
        i, j = curr
        # breaking the next position into y and x
        y, x = next_pos

        # increasing dist by the maximum of the x and y distance between current and next position
        dist += max((abs(y-i)), abs(x-j))

        # updating current position to the next position
        curr = next_pos
    
    return dist

# DRIVER CODE
print(get_min_steps([]))
print(get_min_steps([(0, 0)]))
print(get_min_steps([(0, 0), (1, 1), (1, 2)]))
print(get_min_steps([(0, 0), (1, 1), (1, 2), (3, 4)]))
print(get_min_steps([(0, 0), (1, 1), (1, 2), (3, 6)]))