"""
Problem:

What does the below code snippet print out? How can we fix the anonymous functions to
behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""

# The code is expected to print 9, 9, ..., 9 (10 times) as the value of i is set to 9
# at the end of the 1st loop and is not changed during iterating through the 2nd loop.
# Considering we plan to print 0 to 9, we can set and update the value of i every
# iteration

functions = []
for i in range(10):
    functions.append(lambda: i)

i = 0  # MODIFICATION
for f in functions:
    print(f())
    i += 1  # MODIFICATION
