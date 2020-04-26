'''
Problem:

Given a list of words, return the shortest unique prefix of each word. 

Example:

Input = ["dog", "cat", "apple", "apricot", "fish"]
Output = ["d", "c", "app", "apr", "f"]
'''

# helper function to get the unique prefix for the current word
def get_unique(dictionary, string, string_list):
    # prefix stores the current prefix
    prefix = ""

    # iterating through the word
    for char in string:
        # updating prefix
        prefix += char

        # if the prefix doesn't exist in the dictionary, its returned
        if (prefix not in dictionary):
            return prefix
        else:
            # if the prefix exists, the prefix of the word which collided with the current prefix is updated
            # updation takes place by adding another character to the respective prefixes from both the current and collided word
            # if the current word or the collided word ends before finding a proper prefix, None is returned
            temp_str = string_list[dictionary[prefix]]
            temp_pre = prefix
            temp_pos = dictionary[prefix]

            del dictionary[prefix]

            try:
                temp_pre = temp_str[:len(temp_pre)+1]
            except:
                return None

            dictionary[temp_pre] = temp_pos
    
    return None

# FUNCTION TO PERFORM THE OPERATION
def unique_prefix(string_list):
    # dictionary maps the prefix to the index of the word
    dictionary = {}

    # enumerating through the list of strings
    for index, string in enumerate(string_list):
        # getting the prefix for the current word
        prefix = get_unique(dictionary, string, string_list)

        # if unique prefix doesn't exist, ValueError is raised
        if (not prefix):
            raise ValueError("Unique Prefix Generation not possible")

        # the prefix is updated in the dictionary
        dictionary[prefix] = index
    
    # returning the list of prefixes
    return list(dictionary.keys())

# DRIVER CODE
print(unique_prefix(['dog', 'cat', 'apple', 'apricot', 'fish']))