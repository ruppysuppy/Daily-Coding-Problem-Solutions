'''
Problem:

Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
'''

# reverse function implementation
def reverse(lst, i, j):
    lst[i:j+1] = lst[i:j+1][::-1]

# FUNCTION TO PERFORM THE OPERATION
def sort(lst):
    # using basic bubble sort to sort the entire list
    length = len(lst)

    for i in range(length-1):
        for j in range(length-i-1):
            # reversing the items if the value at position j is larger than that at position i
            if (lst[j] > lst[j+1]):
                reverse(lst, j, j+1)
    
    return lst

# DRIVER CODE
print(sort([0, 6, 4, 2, 5, 3, 1]))
print(sort([0, 6, 4, 2, 5, 3, 1, 10, 9]))
print(sort([0, 6, 4, 2, 5, 3, 1, 2, 3]))
print(sort([0, 6, 4, 2, 5, 3, 1, 11]))