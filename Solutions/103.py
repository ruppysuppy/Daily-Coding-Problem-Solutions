'''
Problem:

Given a string and a set of characters, return the shortest substring containing all the characters in the set.
If there is no substring containing all the characters in the set, return null.

Example:

Input = "figehaeci", {a, e, i}
Output = "aeci"
'''

# FUNCTION TO PERFORM THE OPERATION
def shortest_substring_with_all_characters(string, characters):
    # curr_queue stores the characters considered in the result
    curr_queue = []
    # ind_queue stores the indices considered in the result
    ind_queue = []
    # curr_seen stores the number of required characters in the part under consideration
    curr_seen = set()
    
    # num_char stores the number of characters to consider (length of the passed character set)
    num_char = len(characters)
    # result is the final result
    result = None

    # looping over the string
    for i in range(len(string)):
        # if the current character is in the required characters, its added to curr_queue
        # the index is added to ind_queue and the character to the curr_seen set
        if (string[i] in characters):
            curr_queue.append(string[i])
            ind_queue.append(i)
            curr_seen.add(string[i])
        
        # getting the required shift (to shorten the substring)
        shift = 0
        for k in range(len(curr_queue)//2):
            if (curr_queue[k] == curr_queue[-k-1]):
                shift += 1
        # truncating the queues
        curr_queue = curr_queue[shift:]
        ind_queue = ind_queue[shift:]

        # if all the necessary characters have been found
        if (len(curr_seen) == num_char):
            # if the result is None or the length of the result is larger than the one constructed, its updated
            if ((not result) or (len(result) > (ind_queue[-1] - ind_queue[0] + 1))):
                result = string[ind_queue[0]:ind_queue[-1]+1]

    return result

# DRIVER CODE
print(shortest_substring_with_all_characters("abcdedbc", {'g', 'f'}))
print(shortest_substring_with_all_characters("abccbbbccbcb", {'a', 'b', 'c'}))
print(shortest_substring_with_all_characters("figehaeci", {'a', 'e', 'i'}))
print(shortest_substring_with_all_characters("abcdedbc", {'d', 'b', 'b'}))
print(shortest_substring_with_all_characters("abcdedbc", {'b', 'c'}))
print(shortest_substring_with_all_characters("abcdecdb", {'b', 'c'}))
print(shortest_substring_with_all_characters("abcdecdb", {'b', 'c', 'e'}))