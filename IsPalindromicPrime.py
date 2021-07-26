#isPalindromicPrime() Write a function isPalindromicPrime that takes a value n as a parameter 
#and returns True if the given n is a palindrome and prime and False otherwise.

def palindrome(p):
	p = str(p)
	if(p == p[::-1]):
		return True
	return False

def prime(p):
	if(p==2 or p==3):
		return True
	if(p<2 or p%2==0):
		return False

	if(p>3):
		for i in range(3,p//2):
			if(p%i==0):
				return False
		return True

def isPalindromicPrime(n):
	if(prime(n) == True and palindrome(n) == True):
		return True
	else:
		return False

assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")