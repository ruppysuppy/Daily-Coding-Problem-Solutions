"""
Problem:

There are N prisoners standing in a circle, waiting to be executed. 
The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.
Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.
Bonus: Find an O(log N) solution if k = 2.

Example:

N = 5
k = 2
Output = 3 (sequence will be [2, 4, 1, 5, 3])
"""


def find_last(n, k):
    prisoners = [i for i in range(1, n + 1)]
    last_executed = None
    curr_pos = 0

    while prisoners:
        curr_pos = (curr_pos + k - 1) % len(prisoners)
        last_executed = prisoners[curr_pos]

        prisoners = prisoners[:curr_pos] + prisoners[curr_pos + 1 :]

    return last_executed


print(find_last(5, 2))
print(find_last(3, 2))
print(find_last(5, 3))
