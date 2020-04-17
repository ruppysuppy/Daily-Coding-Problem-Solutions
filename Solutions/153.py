'''
Problem:

Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

Example:

Input = "hello", "world", "dog cat hello cat dog dog hello cat world"
Output = 1 (as there's only one word "cat" in between the two words)
'''

# FUNCTION TO PERFORM THE OPERATION
def dist_calc(text, word1, word2):
    # getting the list of words
    word_list = text.split()
    # getting the number of words
    length = len(word_list)
    # initializing dist, pos and last
    dist = None
    pos = None
    last = None

    # iterating over the list of words
    for i in range(length):
        # if the current word is a match
        if (word_list[i] == word1 or word_list[i] == word2):
            # if the last has not been set, its updated along with pos
            if (last == None):
                last = word_list[i]
                pos = i
            # if the same word is encountered again, pos is updated
            elif (last == word_list[i]):
                pos = i
            else:
                # the last and pos values are updated and temp stores the current distance
                temp = temp = i - pos - 1
                last = word_list[i]
                pos = i

                # the minimum distance is stored in dist
                if (dist == None):
                    dist = temp
                else:
                    dist = min(dist, temp)
    
    return dist

# DRIVER CODE
print(dist_calc("dog cat hello cat dog dog hello cat world", "hello", "world"))
print(dist_calc("dog cat hello cat dog dog hello cat world", "world", "dog"))
print(dist_calc("hello world", "hello", "world"))
print(dist_calc("hello", "hello", "world"))