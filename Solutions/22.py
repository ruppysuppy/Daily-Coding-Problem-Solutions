"""
Problem:

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.


Example:

Input = ['quick', 'brown', 'the', 'fox'], "thequickbrownfox"
Output = ['the', 'quick', 'brown', 'fox']

Input = ['bed', 'bath', 'bedbath', 'and', 'beyond'], "bedbathandbeyond"
Output = ['bed', 'bath', 'and', 'beyond] OR ['bedbath', 'and', 'beyond']
"""

# FUNCTION TO PERFORM THE OPERATION
def words(List, string):
    # Using a set to get O(1) time access to the words
    Set = set()
    # Buffer to store the word formed till the i'th position
    buffer = ""
    # List to store the words forund
    found = []

    # Populating the set for fast access
    for i in List:
        Set.add(i)

    # Looping over the string
    for i in string:
        buffer += i

        # If the word in the buffer is in the set, it is added to the found list and buffer reset
        if buffer in Set:
            found.append(buffer)
            buffer = ""

    # If no word is found, None is returned
    if len(found) == 0:
        return None

    return found


# DRIVER CODE
print(words(["quick", "brown", "the", "fox"], "thequickbrownfox"))
print(words(["bed", "bath", "bedbath", "and", "beyond"], "bedbathandbeyond"))
print(words(["quick", "brown", "the", "fox"], "bedbathandbeyond"))
