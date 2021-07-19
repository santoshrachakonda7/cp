# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	#distance betwwen points
	d1 = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
	d2 = (((x3 - x2) ** 2) + ((y3 - y2) ** 2)) ** 0.5
	d3 = (((x1 - x3) ** 2) + ((y1 - y3) ** 2)) ** 0.5
	return areaoftriangle(d1, d2, d3)

def areaoftriangle(s1, s2, s3):
	if((s1 + s2 <= s3) or (s2 + s3 <= s1) or (s3 + s1 <= s2)):
		return 0
	else:
		# heron's formula
		z = (s1 + s2 + s3)/2
		a = ((z * (z - s1) * (z - s2) * (z - s3)) ** 0.5)
		return a