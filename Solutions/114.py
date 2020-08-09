"""
Problem:

Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. 
Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"

Example:

Input = "hello/world:here"
Output = "here/world:hello"
"""

# FUNCTION TO PERFORM THE OPERATION
def rev_words(string, delimiters):
    # if the string is empty, its returned
    if len(string) == 0:
        return string

    # words stores the words in the string
    words = []
    # delims stores the delimiters in the string
    delims = []
    # flag_beg checks whether the 1st character is a delimiter
    flag_beg = string[0] in delimiters
    # flag_delim checks whether the current string is a delimiter
    flag_delim = False
    # temp stores the current part of the string (word or delimiter)
    temp = ""

    # iterating over the string
    for char in string:
        # if the character is a delimiter
        if char in delimiters:
            # if temp contains delimiters
            if flag_delim:
                # the character is added to temp
                temp += char
            else:
                # if temp contained a word, its added to word list
                if temp:
                    words.append(temp)
                # temp is set to the current delimiter and flag_delim is set
                temp = char
                flag_delim = True
        # if the character is not a delimiter
        else:
            # if temp contains delimiters, flag is reset, temp is added to delimiters and set to the current character
            if flag_delim:
                flag_delim = False
                delims.append(temp)
                temp = char
            # else, the character is added to temp
            else:
                temp += char

    # if the last character is a delimiter, its added to delimiter
    if flag_delim:
        delims.append(temp)
    # else its added to words
    else:
        words.append(temp)

    # reversing the word list and adding empty strings at the end of both lists to avoid index errors
    words = words[::-1]
    words.append("")
    delims.append("")

    # getting the length of the words
    len_words = len(words)
    len_delims = len(delims)
    # i, j are position markers for words and delimiters respectively
    i = 0
    j = 0
    # res stores the final string
    res = ""

    # if flag_beg is set, we add the 1st delimiter and increment j
    if flag_beg:
        j = 1
        res += delims[0]

    # looping till the end of the end of the lists
    while i < len_words or j < len_delims:
        # checking for exceptions
        try:
            # adding the words and delimiters and incrementing i and j
            res += words[i]
            res += delims[j]
            i += 1
            j += 1
        # if index error occours, the control breaks out of the loop
        except IndexError:
            break

    return res


# DRIVER CODE
print(rev_words("hello/world:here", [":", "/"]))
print(rev_words("here/world:hello", [":", "/"]))
print(rev_words("hello/world:here/", [":", "/"]))
print(rev_words("hello//world:here", [":", "/"]))
print(rev_words("hello", [":", "/"]))
print(rev_words("//:", [":", "/"]))
