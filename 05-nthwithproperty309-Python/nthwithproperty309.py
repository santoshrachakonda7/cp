# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def isproperty(n):
	# Your code goes here
	p = str(n**5)
	numbers = ['0','1','2','3','4','5','6','7','8','9']
	for i in numbers:
		if i not in p:
			return False
	return True

def nthwithproperty309(n):
	# Your code goes here
	if(n == 0):
		return 309
	else:
		c = 1
		d = 309
		while(c <= n):
			d = d+1
			if(isproperty(d)):
				c = c + 1
		return d