'''
Problem:

Create a function which takes a function fn and an integer n as an arguement and executes fn after n milli-seconds
'''

# Library import for sleep function

from time import sleep

# Print Hello Function
def print_hello():
    print("Hello!")

# Function to convert milli-second to second
def converter(time_mil):
    time_sec = time_mil / 1000
    return time_sec

# FUNCTION TO PERFORM THE OPERATION
def func(fn=print_hello, n=1000):
    # Delaying by the necessary time
    sleep(converter(n))

    # Executing the function passed as arguement
    fn()

# DRIVER CODE
func(print_hello, 1)
func(print_hello, 500)
func(print_hello, 1000)