'''
Problem:

Given a function f, and N return a debounced f of N milliseconds.
That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.
'''

# import from the time module
from time import sleep

# debounce decorator function
def debounce(s):
    # converting milliseconds to seconds
    interval = s / 1000

    # decorate function
    def decorate(f):
        # wrapped function (with all arguements)
        def wrapped(*args, **kwargs):
            # waiting
            print("\nwaiting initiated...")
            sleep(interval)
            print("waiting over...")

            # calling the function
            return f(*args, **kwargs)
        # returning the wrapped function
        return wrapped
    # returning the decorate function
    return decorate


# FUNCTION TO PERFORM THE OPERATION
@debounce(3000)     # decorator function to implement debouncing
# ordinary addition function
def add_nums(x, y):
    return x + y

# DRIVER CODE
print(add_nums(1, 1))
print(add_nums(1, 2))
print(add_nums(1, 3))
print(add_nums(1, 4))