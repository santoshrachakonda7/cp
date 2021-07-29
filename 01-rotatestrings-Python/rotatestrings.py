# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	#if positive
	if(n > 0):
		while(abs(n)>len(s)):
			n = n - len(s)
		#left rotation
		l1 = s[0:n]
		l2 = s[n:]
		return l2+l1
	#if negative
	else:
		while(abs(n)>len(s)):
			n = n + len(s)
		n = abs(n)
		#right rotation
		r1 = s[0:len(s)-n]
		r2 = s[len(s)-n:]
		return r2+r1
	#return s

