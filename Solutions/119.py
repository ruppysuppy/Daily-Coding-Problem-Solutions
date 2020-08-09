"""
Problem:

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. 
If there are multiple smallest sets, return any of them.

Example:

Input = [[0, 3], [2, 6], [3, 4], [6, 9]]
Output = [3, 6]
"""

# FUNCTION TO PERFORM THE OPERATION
def get_spanning_interval(intervals):
    # setting the start of the spanning interval
    start = intervals[0][1]
    # setting the end of the spanning interval
    end = start
    # pos stores the number of intervals included in the first interval
    pos = 1

    # getting the number of intervals included in the 1st interval
    for interval in intervals[1:]:
        if interval[0] < start and interval[1] < start:
            start = interval[1]
            pos += 1
        else:
            break

    # updating the value of end by iterating through the intervals and checking
    for interval in intervals[pos:]:
        if interval[0] > end:
            end = interval[0]

    # returning a tuple of start and end
    return start, end


# DRIVER CODE
print(get_spanning_interval([[0, 3]]))
print(get_spanning_interval(([[0, 3], [2, 6]])))
print(get_spanning_interval(([[0, 3], [2, 6], [3, 4]])))
print(get_spanning_interval(([[0, 3], [2, 6], [3, 4], [6, 7]])))
print(get_spanning_interval(([[0, 3], [2, 6], [3, 4], [6, 9]])))
print(get_spanning_interval(([[0, 3], [2, 6], [3, 4], [6, 100]])))
print(get_spanning_interval([[0, 4], [1, 2], [5, 6]]))
