"""
Problem:

Write an algorithm to justify text. 
Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
More specifically, you should have as many words as possible in each line. There should be at least one space between each word. 
Pad extra spaces when necessary so that each line has exactly length k. 
Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k

Example:
Input = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],16
Output =    ["the  quick brown", # 1 extra space on the left
            "fox  jumps  over", # 2 extra spaces distributed evenly
            "the   lazy   dog"] # 4 extra spaces distributed evenly
"""

# FUNCTION TO PERFORM THE OPERATION
def justify(word_list, k):
    # Declaring necessary variables:
    # res: stores the result
    # temp: stores the words per line
    # length: total length for the line (1 space included)
    res = []
    temp = []
    length = 0

    # Looping over the list of words
    for i in word_list:
        # if no words have been added to temp
        if temp == []:
            # if the word is longer than k, no justification is possible
            if len(i) > k:
                return [None]
            # else the word is added to temp and length updated
            else:
                temp.append(i)
                length = len(i)

        # if after the adding the current word, the length is within the limit, its added to temp and length updated
        elif len(i) + length + 1 <= k:
            temp.append(i)
            length += len(i) + 1

        # if after the adding the current word, the length oversteps the limit
        elif len(i) + length + 1 > k:
            # if the word is longer than k, no justification is possible
            if len(i) + 1 > k:
                return [None]
            # Adding the final result to res
            else:
                # Extra spaces left
                extra = k - length

                # if only 1 word is present, extra padding is added to the right
                if len(temp) == 1:
                    res.append(temp[0] + " " * extra)

                # if the space can be equally distributed, it is done so
                elif extra % (len(temp) - 1) == 0:
                    res.append((" " * (extra // (len(temp) - 1) + 1)).join(temp))

                # if the space cannot be equally distributed, extra spaces are added betweens the words, starting from the left
                else:
                    extra_extra = extra % (len(temp) - 1)
                    regular = extra // (len(temp) - 1) + 1

                    temp_str = ""

                    for i in temp:
                        temp_str += i + " " * regular

                        if extra_extra:
                            temp_str += " "
                            extra_extra -= 1

                    res.append(temp_str.rstrip())

                # updating temp and length
                temp = [i]
                length = len(i)

    # operation after the iteration is complete (to add the last set of word(s))
    if temp != []:
        # Extra spaces left
        extra = k - length

        if len(temp) == 1:
            res.append(temp[0] + " " * extra)

        # if the space can be equally distributed, it is done so
        elif extra % (len(temp) - 1) == 0:
            res.append((" " * (extra // (len(temp) - 1) + 1)).join(temp))

        # if the space cannot be equally distributed, extra spaces are added betweens the words, starting from the left
        else:
            extra_extra = extra % (len(temp) - 1)
            regular = extra // (len(temp) - 1) + 1

            temp_str = ""

            for i in temp:
                temp_str += i + " " * regular

                if extra_extra:
                    temp_str += " "
                    extra_extra -= 1

            res.append(temp_str.rstrip())

    return res


# DRIVER CODE
for i in justify(
    ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "Done"], 16
):
    # NOTE: Using the "'"s is not important, used it to denote thestart and end of the string (helpful in case of 1 word in 1 line)
    print("'" + i + "'")
