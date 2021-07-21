# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# Your code goes here
	count_d1 = 0
	count_d2 = 0
	l1 = []
	l2 = []
	if(len(a) == len(a[0])):
		for i in range(0, len(a)):
			count_d1 += a[i][i]
			count_d2 += a[i][len(a)-i-1]
			r = 0
			c = 0
			for j in range(0, len(a[0])):
				r += a[i][j]
				c += a[j][i]
			l1.append(r)
			l2.append(c)
			l1 = list(set(l1))
			l2 = list(set(l2))

			if(len(l1) == len(l2) == 1 and 
			l1[0] == l2[0] == count_d1 == count_d2):
				return True
	return False
