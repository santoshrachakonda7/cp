# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.




def fun_getaverage(s): 
	#converting to a list
	t = s.split(",")
	li = []
	for i in t:
		#putting only the integers into a list
		if(i.isdigit()):
			li.append(int(i))
	#if list is empty
	if(len(li) == 0):
		return 0.0
	#if list is not empty, find average
	else:
		a = 0
		for j in li:
			a = a + j
	
		b = a/len(li)
		return b