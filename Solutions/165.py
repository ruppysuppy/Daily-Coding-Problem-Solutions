'''
Problem:

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

Example:

Input = [3, 4, 9, 6, 1]
Output = [1, 1, 2, 1, 0]
(
Since:
* There is 1 smaller element to the right of 3
* There is 1 smaller element to the right of 4
* There are 2 smaller elements to the right of 9
* There is 1 smaller element to the right of 6
* There are no smaller elements to the right of 1
)
'''

# FUNCTION TO PERFORM THE OPERATION
def smaller_elem_arr_construct(arr):
    # using brute force to solve the problem [O(n^2) algorithm]
    # small array stores the result
    small_arr = []
    # getting the length of the input array
    length = len(arr)

    # iterating through the input array
    for i in range(length):
        # getting the smaller elements to the right count
        smaller_elements = 0

        # updating smaller_elements
        for j in range(i+1, length):
            if (arr[i] > arr[j]):
                smaller_elements += 1
        
        # updating smaller_arr
        small_arr.append(smaller_elements)
    
    # returning the resultant array
    return small_arr

# DRIVER CODE
print(smaller_elem_arr_construct([3, 4, 9, 6, 1]))

# NOTE: This problem can be solved in O(nlogn) using AVL Tree, but the algorithm is complex to understand