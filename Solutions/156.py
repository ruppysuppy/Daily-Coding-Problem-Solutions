'''
Problem:

Given a positive integer n, find the smallest number of squared integers which sum to n.

Example:

Input = 13
Output = 2 (since 13 = 3^2 + 2^2 = 9 + 4)

Input = 27
Output = 3 (since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9)
'''

# FUNCTION TO PERFORM THE OPERATION
def min_sq_num(num, accumulator=0):
    # base case for recursion 1
    if (num == 0):
        return accumulator
    # base case for recursion 2
    elif (num == 1):
        return (accumulator + 1)

    else:
        # getting the largest square number that is smaller than the current number
        largest_sq_divisor = int(num ** 0.5) ** 2

        # updating the number and incrementing accumulator
        num = num - largest_sq_divisor
        accumulator += 1

        # calling the function recursively
        return min_sq_num(num, accumulator)

# DRIVER CODE
print(min_sq_num(25)) # (5 ^ 2)
print(min_sq_num(13)) # (2 ^ 2) + (3 ^ 2)
print(min_sq_num(27)) # (5 ^ 2) + (1 ^ 2) + (1 ^ 2)