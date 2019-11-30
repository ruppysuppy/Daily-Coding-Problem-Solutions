'''
Problem:

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, "abcba", 2 => 'bcb'
'''

# FUNCTION TO PERFORM THE OPERATION
def longest_substring_k_unique(string, k, length):
    # Declaring vaiables
    # start and end is used to create the window (end - start)
    start = 0
    end = 1
    longest_substring_till_now = string[0]
    # Hash map to store the number of occourance of the character in the present window
    hash_map = {string[0]: 1}
    num_unique = 1

    # Loop to go over the entire string
    while (end < (length)):
        # if the last character is already in the longest_substring_till_now, the value in the map is incremented
        if (string[end] in hash_map and hash_map[string[end]] != 0):
            hash_map[string[end]] += 1
        
        else:
            # if the last value is not in longest_substring_till_now, the value in the map is incremented
            # num_unique is incremented
            hash_map[string[end]] = 1
            num_unique += 1

            # if the number of unique characters excede k, then 1 by 1 charcters are removed from the start, till there are k unique values
            if (num_unique > k):
                while (num_unique > k):
                    hash_map[string[start]] -= 1
                    if (hash_map[string[start]] == 0):
                        num_unique -= 1
                    start += 1

        # forming the new string
        temp = string[start: end+1]

        # if the new string is longer than longest_substring_till_now, longest_substring_till_now is overwritten
        if (num_unique == k and len(temp) > len(longest_substring_till_now)):
            longest_substring_till_now = temp
        
        end += 1
    
    # if the number of unique charcters is equal to k, the longest_substring_till_now is returned
    # else and empty string is returned (if there are less than k unique characters in s)
    if (num_unique == k):
        return longest_substring_till_now
    else:
        return ''

# DRIVER CODE
print(longest_substring_k_unique("abcba", 2, len("abcba")))
print(longest_substring_k_unique("abcba", 20, len("abcba")))
print(longest_substring_k_unique("karappa", 2, len("karappa")))