'''
Problem:

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock. 
You're also given a number fee that represents a transaction fee for each buy and sell transaction.
You must buy before you can sell the stock, but you can make as many transactions as you like.

Example:

Array = [1, 3, 2, 8, 4, 10]
Fee = 2
Output = 9 
(Since you could buy the stock at $1, and sell at $8, and then buy it at $4 and sell it at $10.
Since we did two transactions, there is a $4 fee, so we have 7 + 6 = 13 profit minus $4 of fees.)
'''

# FUNCTION TO PERFORM THE OPERATION
def get_max_profit(prices, fee, profit=0, current=0, can_buy=True):
    # if the price array is empty, the profit is returned
    if (not prices):
        return profit
    
    # if buying is permitted, checking for holding the stock and buying at the current price
    if (can_buy):
        return max(
            get_max_profit(prices[1:], fee, profit, -prices[0]-fee, False),
            get_max_profit(prices[1:], fee, profit, 0, True)
        )
    # if selling is permitted, checking for holding the stock and selling at the current price
    else:
        return max(
            get_max_profit(prices[1:], fee, profit+(current+prices[0]), 0, True),
            get_max_profit(prices[1:], fee, profit, current, False)
        )

# DRIVER CODE
print(get_max_profit([1, 3, 2, 8, 4, 10], 2))
print(get_max_profit([1, 3, 2, 1, 4, 10], 2))