"""
Problem:

A builder is looking to build a row of N houses that can be of K different colors. 
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost.
"""

# FUNCTION TO PERFORM THE OPERATION
def minimizeColorCost(arr, n, k):
    # array to store the possible sequences
    results = []

    # calling the helper function
    helper(arr, results, 0, -1, 0, "", n, k)

    return min(
        results
    )  # USE 'return min(results, key=lambda x: x[0])' incase you want to return the sequence too


# helper function to carry out the main operations (Uses Recursion)
def helper(arr, results, curr_house, prev_color, curr_cost, curr_sequence, n, k):
    # Base case, the sequence has been generated
    if curr_house == n:
        # adding the cost to the result array
        results.append(
            curr_cost
        )  # USE 'results.append((curr_cost, curr_sequence))' to add the sequence too
        return

    # Loop to generate all the possible combinations
    for i in range(k):
        # When the current color is not equal to the previous color the helper function is called to generate the sequence
        if i != prev_color:
            helper(
                arr,
                results,
                curr_house + 1,
                i,
                arr[curr_house][i] + curr_cost,
                curr_sequence + str(i),
                n,
                k,
            )


# DRIVER CODE
mat1 = [[1, 5, 2], [2, 3, 1], [7, 3, 5], [6, 2, 3]]
mat2 = [[1, 5, 2], [2, 3, 1], [7, 3, 5], [6, 3, 2]]
n = 4
k = 3

print(minimizeColorCost(mat1, n, k))
print(minimizeColorCost(mat2, n, k))
