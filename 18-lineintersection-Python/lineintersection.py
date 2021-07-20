# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
	# your code goes here
	if(m1 == m2 or b1 == b2):
		return None
	
	elif(fun_ismultiple(m1, m2) or fun_ismultiple(m2,m1)):
		return None
	#formula for line intersection
	else:
		a = (b2 - b1)/(m1 - m2)
		return a
	
def fun_ismultiple(m,n):
	if((m == n) or (n!=0 and m%n == 0)):
		return True
	return False
