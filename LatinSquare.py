# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    # Your code goes here...
    s = set(j for i in lst for j in i)
    t = zip(*lst)
    for i,j in zip(lst,t):
        for k in s:
            if k not in i or k not in j:
                return False
    return True

print(isLatinSquare([["x", "y", "z"],["z", "x", "y"],
["y", "z", "x"]]))
print(isLatinSquare([[1, 1, 1], [1, 2, 2], [1, 3, 3], [2, 1, 2], [2, 2, 3], [2, 3, 1], [3, 1, 3], [3, 2, 1], [3, 3, 2]]))
