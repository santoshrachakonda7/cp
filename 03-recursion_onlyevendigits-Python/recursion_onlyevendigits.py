# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def foreven(n, k=0):
	if(n != 0):
		if((n % 10) % 2 == 0):
			return foreven(n // 10, k = (k * 10) + (n % 10))
		else:
			return foreven(n // 10, k)
		
	else:
		return k

def even_num(t, k=0):
	if(t != 0):
		return even_num(t // 10, k = k * 10 + t % 10)
		
	else:
		return k

def result(q, m):
	if(len(q) != m):
		a = q[m]
		q[m] = even_num(foreven(a))
		return result(q, m + 1)

	else:
		return q

def fun_recursion_onlyevendigits(l): 
		if len(l) == 0:
			return []
		else:
			return result(l, 0)