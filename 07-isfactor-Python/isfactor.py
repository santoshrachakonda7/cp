# Write the function isFactor(f, n) that takes 
# two int values f and n, and returns True 
# if f is a factor of n, and False otherwise. 
# Note that every integer is a factor of 0.



def fun_isfactor(f, n):
	#if both are equal
	if(f==n):
		return True
	#return false if f=0
	elif(f==0):
		return False
	#check factorization
	elif(n%f == 0):
		return True
	
	return False # replace with your solution
