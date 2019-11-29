'''
Problem:

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

EXAMPLE:

input = 4
output = 5
'''

# FUNCTION TO PERFORM THE OPERATION
def count_ways(steps, permissable_setps=[1,2]):
    # Dynamic Programming to reduce time complexity to O(n)
    # Array to store the number of ways a step can be reached
    dynamic_arr = [0 for i in range(steps+1)]

    # Setting the number of ways 0 can be reached (1 = Not using any permissible steps)
    dynamic_arr[0] = 1

    # calculating using the formula steps_i = sum(steps_(i-j)) [i = [0, steps], j = [values in permissable_setps]]
    # the sequence genearted is SIMILAR to fibonacci series
    for pos in range(steps+1):
        for step in permissable_setps:
            temp = pos - step

            if (temp >= 0):
                dynamic_arr[pos] += dynamic_arr[temp]
    
    # After filling up the values, the value at i'th position indicates the number of ways one can traverse i steps using the permissable_setps
    return dynamic_arr[steps]

# DRIVER CODE
print(count_ways(4))
print(count_ways(1, [1, 3, 5]))
print(count_ways(2, [1, 3, 5]))
print(count_ways(3, [1, 3, 5]))
print(count_ways(4, [1, 3, 5]))
print(count_ways(5, [1, 3, 5]))
print(count_ways(6, [1, 3, 5]))