"""
Problem:

You are given an array of numbers representing the stock prices of a company in chronological order and an integer k. 
Return the maximum profit you can make from k buys and sells. 
You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

Example:

Input = [5, 2, 4, 0, 1], 2
Output = 3
"""

# helper function for the computation
def max_profit_helper(arr, curr_index, curr_profit, buys_left, sells_left):
    # if the end of the array is reached or no more sells can be performed
    # current profit is returned (base case for recursion)
    if curr_index == len(arr) or sells_left == 0:
        return curr_profit

    # if the number of buys left and sells left are equal, we have to buy a stock
    if buys_left == sells_left:
        # returning the max profit we can obtain
        return max(
            # wait for a different deal
            max_profit_helper(arr, curr_index + 1, curr_profit, buys_left, sells_left),
            # buy at the current price
            max_profit_helper(
                arr,
                curr_index + 1,
                curr_profit - arr[curr_index],
                buys_left - 1,
                sells_left,
            ),
        )
    # if the number of buys left and sells left are inequal, we have to sell a stock
    else:
        # returning the max profit we can obtain
        return max(
            # wait and hold for selling at a different price
            max_profit_helper(arr, curr_index + 1, curr_profit, buys_left, sells_left),
            # sell at the current price
            max_profit_helper(
                arr,
                curr_index + 1,
                curr_profit + arr[curr_index],
                buys_left,
                sells_left - 1,
            ),
        )


# FUNCTION TO PERFORM THE OPERATION
def max_profit(arr, k):
    # offloading the computation to the helper function
    return max_profit_helper(arr, 0, 0, k, k)


# DRIVER CODE
print(max_profit([5, 2, 4, 0, 1], 2))
print(max_profit([5, 2, 4], 2))
print(max_profit([5, 2, 4], 1))
