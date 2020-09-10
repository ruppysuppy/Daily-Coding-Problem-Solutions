"""
Problem:

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. 
You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. 
If there's no way to break the text up, then return null.
You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

Example:

"the quick brown fox jumps over the lazy dog", 10 => ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
"""

# FUNCTION TO PERFORM THE OPERATION
def break_string(string, k):
    # str_list: stores the list of words (input)
    # word_list: stores the list of words (output)
    # curr_len: stores the length of the current output
    # curr_str: stores the current output string
    str_list = string.split()
    word_list = []
    curr_len = 0
    curr_str = ""

    # looping over the words (input)
    for i in str_list:
        temp = len(i)

        # if the loop is just starting this conditional is entered
        if curr_len == 0:
            # if the word length is larger than k, None is returned, else curr_len and curr_str are updated
            if temp < k:
                curr_len = temp
                curr_str = i
            else:
                return None

        # if the word length is larger than k, None is returned, else word_list, curr_len and curr_str are updated
        elif curr_len + temp + 1 > k:
            if temp > k:
                return None

            word_list.append(curr_str)
            curr_str = i
            curr_len = temp

        # the current word can be incorporated in the curr_str if its possible
        else:
            curr_len += temp
            curr_str += " " + i

    # adding the final string and returning the word_list
    word_list.append(curr_str)
    return word_list


# DRIVER CODE
print(break_string("the quick brown fox jumps over the lazy dog", 10))
print(break_string("the quick brown fox jumps over the lazy dog", 3))
