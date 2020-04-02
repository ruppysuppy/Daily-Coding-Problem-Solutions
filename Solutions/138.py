'''
Problem:

Find the minimum number of coins required to make n cents.
You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

Example:

Input = 16
Output = 3 (10¢, a 5¢, and a 1¢)
'''

# FUNCTION TO PERFORM THE OPERATION
def calc_num_coins(target, amt_arr=[1, 5, 10, 25]):
    # this method considers that the denominations are sorted, if that is not the case, we have to sort them
    # getting the length of the amount array
    length = len(amt_arr)
    # count stores the number of coins used
    count = 0

    # checking all the coins in the amount array
    for i in range(length-1, -1, -1):
        # adding the number of current coins that can be used optimally
        count += (target // amt_arr[i])
        # updating target
        target = target % amt_arr[i]
        # breaking out of the loop if we have reached the target
        if (target == 0):
            break
    
    # returning the number of coins or raising ValueError if the target cannot be reached
    if (target == 0):
        return count
    else:
        raise ValueError("Target cannot be reached by using the supplied denominations")

# DRIVER CODE
print(calc_num_coins(16))
print(calc_num_coins(90))
print(calc_num_coins(93))
print(calc_num_coins(100))