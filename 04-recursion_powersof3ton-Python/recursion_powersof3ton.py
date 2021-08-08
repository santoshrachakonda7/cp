# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def powersof3ton(n,li,c):
	p = 3 ** c
	if(p <= n):
		li.append(p)
	c += 1
	if(p >= n):
		return li
	return powersof3ton(n,li,c)


def recursion_powersof3ton(n):
	# Your code goes here
	li=[]
	if(n >= 1):
		return powersof3ton(n,li,0)
	else:
		return None
