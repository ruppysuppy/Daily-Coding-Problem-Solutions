'''
Problem:

Given n integers and a target number, find whether 2 of the given numbers sum up to the
target number.
'''


def check_target_sum(arr, target):
    # using hash list to store the previously seen values to get access to them in O(1)
    previous = set()
    for elem in arr:
        if (target - elem) in previous:
            return True
        previous.add(elem)
    return False


# DRIVER CODE
print(check_target_sum([], 17))
print(check_target_sum([10, 15, 3, 7], 17))
print(check_target_sum([10, 15, 3, 4], 17))


'''
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
'''
