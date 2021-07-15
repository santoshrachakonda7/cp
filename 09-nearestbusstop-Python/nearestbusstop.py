# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	for i in range(0,11):
		
		n = i*8
		s = (i+1)*8
		if(abs(street-n) <=8 and abs(street-s) <= 8):
			if((abs(street-n) < abs(street-s)) or (abs(street-n) == abs(street-s))):
				return n
			elif(abs(street-n) > abs(street-s)):
				return s
		else:
			i=i+1

