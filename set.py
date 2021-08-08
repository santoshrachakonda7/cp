# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]
import itertools
def limitedPowerSet(n, k):
    # Your code goes here...
    u = set(())
    for i in range(1, n+1):
        u.add(i)
    l = [{}]
    for i in range(1, len(u)+1):
        m = list(map(set, itertools.combinations(u, i)))
        for j in range(len(m)):
            if(len(l) != k):
                l.append(m[j])
            else:
                return l

assert(limitedPowerSet(5, 7) == [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ])
print("All test cases passed...")