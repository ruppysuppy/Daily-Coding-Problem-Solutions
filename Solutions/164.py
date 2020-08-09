"""
Problem:

You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. 
By the pigeonhole principle, there must be a duplicate. 
Find it in linear time and space.
"""

# FUNCTION TO PERFORM THE OPERATION
def find_duplicate(arr):
    # seen set to get access to the seen values in O(1) time
    seen = set()

    # iterating through the array and populating seen
    for i in arr:
        # when a previously seen element is encountered again, its returned
        if i in seen:
            return i
        seen.add(i)


# DRIVER CODE
print(find_duplicate([1, 2, 4, 6, 5, 3, 2]))
print(find_duplicate([3, 1, 4, 2, 3]))
