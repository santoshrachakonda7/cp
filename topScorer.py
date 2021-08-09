# topScorer(data) [10 Points]
# Write the function topScorer(data) that takes a multi-line 
# string encoding scores as csv data for some kind of 
# competition with players receiving scores, so each 
# line has comma-separated values. The first value on 
# each line is the name of the player (which you can 
# assume has no integers in it), and each value after 
# that is an individual score (which you can assume is a 
# non-negative integer). You should add all the scores 
# for that player, and then return the player with the 
# highest total score. If there is a tie, return all the 
# tied players in a comma-separated string with the names 
# in the same order they appeared in the original data. 
# If nobody wins (there is no data), return None (not the 
# string "None"). So, for example:

def topScorer(data):
    # Your code goes here...
    if(len(data)==0):
        return None

    s = 0
    n = data.split("\n")
    d = n[0:-1]
    for i in d:
        p = i.split(",")
        t=0
        for j in (p[1:]):
            t = t + int(j)
        if(t > s):
            s = t
            a = d[1].split(",")
            b = a[0]
        elif(t < s):
            a = d[0].split(",")
            b = a[0]
        elif(s == t):
            a1 = d[0].split(",")
            b1 = a1[0]
            a2 = d[1].split(",")
            b2 = a2[0]
            b = (b1 + "," + b2)
    return b

data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
assert(topScorer(data) == 'Fred')

data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
assert(topScorer(data) == 'Wilma')

data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
assert(topScorer(data) == 'Fred,Wilma')

assert(topScorer('') == None)
print("All test cases passed...!")
# Hint: you may want to use both splitlines() and split(',') here!
