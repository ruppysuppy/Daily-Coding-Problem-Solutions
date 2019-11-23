'''
Problem:

Find the 1st missing positive number in the given set of numbers in O(n).
Eg: 1, 2, 3, 4 => 5
'''

# FUNCTION TO PERFORM THE OPERATION
def first_positive_integer(Arr, length):
    # Cache to store the numbers (later used to get access in O(1) time)
    num_cache = set()

    # Populating Cache
    for i in Arr:
        num_cache.add(i)

    # Checking if the number is in cache, if its absent, the value is returned
    # The range goes from 1 to length + 2 (as the range function yields values in [start, stop))
    # In an array of 'length' elements, at most 'length' unique values can be present
    # So we are bound to find a value which is not present ((length+2) - 1 = (length+1))
    for i in range(1, length+2):
        if (i not in num_cache):
            return i

# DRIVER CODE
Arr = [1, 2, 3, 4]#[int(i) for i in input("Enter the elements of the array (separated by space): ").split()]
ans = first_positive_integer(Arr, len(Arr))

print(ans)

'''
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
'''