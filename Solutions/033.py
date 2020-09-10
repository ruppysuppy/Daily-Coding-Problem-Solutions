"""
Problem:
Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.

Example:
Input = [2, 1, 5, 7, 2, 0, 5] 
Output = [2, 1.5, 2, 3.5, 2, 2, 2]
"""

# Helper function to perform insertion sort on the current position (as its applied one after another, so results in a sorted array at the end)
def ins_sort(Arr, element, pos):
    # Setting the value of at the required position
    Arr[pos] = element

    # Looping over till the left of the Array is sorted
    for i in range(pos, 0, -1):
        if Arr[i] < Arr[i - 1]:
            Arr[i], Arr[i - 1] = Arr[i - 1], Arr[i]
        else:
            break

    return Arr


# FUNCTION TO PERFORM THE OPERATION
def running_median(Arr, length):
    # Ans: stores the running median
    # temp: stores the sorted array till the i'th position
    # pos: keeps track of the current position
    Ans = [-9999 for i in range(length)]
    temp = [-9999 for i in range(length)]
    pos = 0

    # Looping over all the elements
    for element in Arr:
        # Performing insertion sort on the temp array and incrementing the position counter
        ins_sort(temp, element, pos)
        pos += 1

        # Calulating and storing the running median
        if pos % 2 != 0:
            Ans[pos - 1] = temp[pos // 2]
        else:
            Ans[pos - 1] = (temp[pos // 2] + temp[pos // 2 - 1]) / 2

    return Ans


# DRIVER CODE
inp = [2, 1, 5, 7, 2, 0, 5]
ans = running_median(inp, len(inp))
print(("{:.2f}\t" * len(ans)).format(*ans))
