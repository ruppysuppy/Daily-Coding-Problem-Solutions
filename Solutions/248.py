"""
Problem:

Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.
"""

# max using bit-wise operations
def get_max(num1, num2):
    return num1 ^ ((num1 ^ num2) & -(num1 < num2))


# DRIVER CODE
print(get_max(1, 5))
print(get_max(4, 3))
print(get_max(-3, 6))
print(get_max(5, -4))
print(get_max(-4, -2))
print(get_max(-3, -6))
