# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
		z = 1
		flag1 = True
		flag2 = True
		while(z<len(a)):
			if(a[z] < a[z-1]):
				flag1 = False
			elif(a[z] > a[z-1]):
				flag2 = False
			z = z + 1
		if(flag1 == True or flag2 == True):
			return True
		else:
			return False
