# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isprime(p):
	if(p==2 or p==3):
		return True
	if(p<2 or p%2==0):
		return False
	if(p>3):
		for i in range(3,p//2):
			if(p%i==0):
				return False
		return True

def issmith(n):
	if(isprime(n)!=True):
		t = n
		fl = []
		s = 0
		if(n == 1):
			return False
		for i in range(2,(n//2) + 1):
			if(isprime(i) == True) and (n%i == 0):
				fl.append(i)
		a = 0
		for j in str(n):
			a += int(j)
		li = []
		for i in fl:
			while (t%i == 0 and t != 0):
				li.append(i)    
				s += i
				t = t//i
		b = 0        
		for j in li:
			if(j > 9):
				for d in str(j):
					b += int(d)
			else:
			   b+=j
		if(a == b):
			return True
		else:
			return False

def fun_nth_smithnumber(n):
	c=0
	f=1
	r = 0
	while(n+1 != c):
		if(issmith(f) == True):
			c+=1
			r = f
		f = f + 1
	return r