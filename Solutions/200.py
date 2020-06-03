'''
Problem:

Let X be a set of n intervals on the real line. 
We say that a set of points P "stabs" X if every interval in X contains at least one point in P. 
Compute the smallest set of points that stabs X.

Example:

Input = [(1, 4), (4, 5), (7, 9), (9, 12)]
Output = [4, 9]
'''

# FUNCTION TO PERFORM THE OPERATION
def get_stabs(list_of_intervals):
    # creating tuples of start and end time
    start, end = zip(*list_of_intervals)
    # returning the minimum value of end (start of stab) and the maximum value for start (end of stab)
    return min(end), max(start)

# DRIVER CODE
print(get_stabs([(1, 4), (4, 5), (7, 9), (9, 12)]))