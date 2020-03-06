'''
Problem:

Given a word W and a string S, find all starting indices in S which are anagrams of W.

Example:

Input = "ab", "abxaba"
Output = [0, 3, 4]
'''

# helper to break the string into a dictionary of characters and number of occourances
def break_char(string):
    d = {}

    for i in string:
        if (i in d):
            d[i] += 1
        else:
            d[i] = 1
    
    return d

# FUNCTION TO PERFORM THE OPERATION
def get_word_start_loc(word, string):
    # getting the length of the word
    word_len = len(word)
    # getting the length of the string
    str_len = len(string)
    # breaking the string into its characters
    needed_master = break_char(word)
    # needed stores the characters left to be found in the string
    needed = dict(needed_master)
    # curr stores the current position
    curr = 0
    # res stores the positions of the anagrams
    res = []

    # if the word is longer than the string, no anagram is possible
    if ((word_len > str_len) or (word_len == 0)):
        return []
    
    # looping till we reach the end of the string
    while (curr < str_len):
        # looping till we reach the end of the string from current position
        # [NOTE: the algo is O(n) evene though it has a nested loop]
        for i in range(curr, str_len):
            # if a character mismatch occours, we break out (incrementing curr + reseting needed)
            if (string[i] not in needed):
                curr = i
                needed = dict(needed_master)
                break
            
            # if the charater is in needed
            elif (string[i] in needed):
                # the character count is reduced by 1
                needed[string[i]] -= 1
                # if the character count reaches 0
                if (needed[string[i]] == 0):
                    # we delete the character from needed
                    del needed[string[i]]

                    # if needed is empty
                    if (needed == {}):
                        # we add the current position to res
                        res.append(curr)
                        # setting curr to the current position
                        curr = i - 1
                        # reseting needed
                        needed = dict(needed_master)
                        break
        
        # incrementing curr
        curr += 1
        
    return res

# DRIVER CODE
print(get_word_start_loc("ab", "abxaba"))
print(get_word_start_loc("tac", "cataract"))