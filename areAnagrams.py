# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    # Your code goes here...
    sl1 = s1.lower()
    sl2 = s2.lower()
    sl3 = []
    if(len(sl1) == len(sl2)):
        for x in sl1:
            for y in sl2:
                if(x == y):
                    sl3.append(x)
        if(len(sl3) == len(sl1)):
            return True
        else:
            return False

    else:
        return False
# write your test cases here...
assert(areAnagrams("abc", "abc") == True)
assert(areAnagrams("aBd", "DeA") == False)
assert(areAnagrams("vdF", "fDVEm") == False)
assert(areAnagrams("ABC", "cab") == True)
print("All test cases passed... :-)")
