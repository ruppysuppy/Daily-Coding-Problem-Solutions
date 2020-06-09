'''
Problem:

A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. 
For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.
Given an array and a permutation, apply the permutation to the array. 

Example:

Array = ["a", "b", "c"] 
Permutation = [2, 1, 0]
Output = ["c", "b", "a"]
'''

# FUNCTION TO PERFORM THE OPERATION
def permute(arr, p):
    # getting the length of the array
    length = len(arr)

    # updating p to hold the result
    for i in range(length):
        p[i] = arr[p[i]]
    
    # returning p
    return p

# DRIVER CODE
print(permute(["a", "b", "c"], [2, 1, 0]))
print(permute(['a', 'b', 'c', 'd'], [2, 1, 0, 3]))