'''
Problem:

One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.
For a pattern to be valid, it must satisfy the following:
* All of its keys must be distinct.
* It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.
Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
'''

from copy import deepcopy


class Dialpad:
    # dial-pad class to hold the nodes and update the connections
    def __init__(self):
        self.nodes = set(range(1, 10))
        self.edges = {}
        self.edges[1] = {2, 4, 5, 6, 8}
        self.edges[2] = {1, 3, 4, 5, 6, 7, 9}
        self.edges[3] = {2, 4, 5, 6, 8}
        self.edges[4] = {1, 2, 3, 5, 7, 8, 9}
        self.edges[5] = {1, 2, 3, 4, 6, 7, 8, 9}
        self.edges[6] = {1, 2, 3, 5, 7, 8, 9}
        self.edges[7] = {2, 4, 5, 6, 8}
        self.edges[8] = {1, 4, 3, 5, 6, 7, 9}
        self.edges[9] = {2, 4, 5, 6, 8}
    
    def update_connections(self, curr):
        # function to update the connections
        if (2 == curr):
            self.edges[1].add(3)
            self.edges[3].add(1)
        elif (4 == curr):
            self.edges[1].add(7)
            self.edges[7].add(1)
        elif (6 == curr):
            self.edges[9].add(3)
            self.edges[3].add(9)
        elif (8 == curr):
            self.edges[7].add(9)
            self.edges[9].add(7)
        elif (5 == curr):
            self.edges[1].add(9)
            self.edges[9].add(1)
            self.edges[7].add(3)
            self.edges[3].add(7)
            self.edges[2].add(8)
            self.edges[8].add(2)
            self.edges[4].add(6)
            self.edges[6].add(4)


def count_code_helper(dp, code_len, curr, seen):
    # helper function to trace the patterns and get the number of combinations
    if code_len == 0:
        return 1
    seen_cp = deepcopy(seen)
    seen_cp.add(curr)

    copied_dp = deepcopy(dp)
    copied_dp.update_connections(curr)
    nodes = dp.edges[curr]
    sub_count = 0

    for node in nodes:
        if node not in seen_cp:
            sub_count += count_code_helper(copied_dp, code_len - 1, node, seen_cp)
    return sub_count


def count_codes(dp, code_len):
    # function to generate the number of combinations of pattens of given length
    if code_len == 1:
        return len(dp.nodes)
    count = 0
    for node in dp.nodes:
        count += count_code_helper(dp, code_len, node, set())
    return count


# FUNCTION TO PERFORM THE OPERATION
def valid_unlock_patterns_number():
    dp = Dialpad()
    result = 0
    for i in range(1, 10):
        temp = count_codes(dp, i)
        result += temp
    return result


# DRIVER CODE
# NOTE: computationally intensive operation as the number of patterns is really high
print(valid_unlock_patterns_number())