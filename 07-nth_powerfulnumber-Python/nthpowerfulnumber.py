# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def nthpowerfulnumber(n):
	# Your code goes here
	i = 0
	j = 0
	while(i <= abs(n)):
		j += 1
		if(isPowerful(j)):
		   i += 1
	return j

def isPowerful(n):
	while(n % 2 == 0):
		z = 0
		while(n % 2 == 0):
			n = n // 2
			z = z + 1
		if(z == 1):
			return False
	for p in range(3, int(n**0.5)+1, 2):
		a = 0
		while(n % p == 0):
			n = n // p
			a = a + 1
		if(a == 1):
			return False
	return n == 1
