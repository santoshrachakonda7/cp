"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    # Your code goes here
    a = input_array[0]
    z = len(input_array) - 1
    while(a<=z):
        #for middle
        k = a + (z - a) // 2
        if(input_array[k] > value):
            z = k - 1
        elif(input_array[k] < value):
            a = k + 1
        else:
            #returning middle element
            return k
    else:
        #if no value exists
        return -1
 