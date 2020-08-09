"""
Problem:

Given a number in the form of a list of digits, return all possible permutations.

Example:

Input = [1,2,3]
Output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

# FUNCTION TO PERFORM THE OPERATION
def permute(arr, l=0, r=None, res=[]):
    # getting the end position (in case it is not passed)
    if r == None:
        r = len(arr) - 1

    # adding the current permutaion in case the end has been reached
    if l == r:
        res.append(list(arr))

    else:
        for i in range(l, r + 1):
            # generating all permutation by changing i'th element with all other elements
            arr[l], arr[i] = arr[i], arr[l]
            # recursive calling
            permute(arr, l + 1, r, res)
            # backtracking
            arr[l], arr[i] = arr[i], arr[l]

    return res


# DRIVER CODE
print(permute([1, 2, 3], res=[]))
print(permute([1, 2], res=[]))
print(permute([1], res=[]))
print(permute([], res=[]))
