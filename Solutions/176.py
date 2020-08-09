"""
Problem:

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

Example:

s1 = 'abc'
s2 = 'bcd'
Output = true (since we can map 'a' to 'b', 'b' to 'c', and 'c' to 'd')

s1 = 'foo'
s2 = 'bar'
Output = false (since the 'o' cannot map to two characters)
"""

# FUNCTION TO PERFORM THE OPERATION
def check(s1, s2):
    # getting the lengths of the strings
    l1 = len(s1)
    l2 = len(s2)

    # creating a dictionary
    d = {}

    # checking if each character of s1 maps to a unique character of s2
    # (part of the condition for one-to-one map)
    for i in range(l1):
        if s1[i] in d and d[s1[i]] != s2[i]:
            return False
        d[s1[i]] = s2[i]

    # creating a dictionary
    d = {}

    # checking if each character of s2 maps to a unique character of s1
    # (part of the condition for one-to-one map)
    for i in range(l2):
        if s2[i] in d and d[s2[i]] != s1[i]:
            return False
        d[s2[i]] = s1[i]

    # returning True if both the conditions are satisfied
    return True


# DRIVER CODE
print(check("abc", "bcd"))
print(check("abc", "foo"))
