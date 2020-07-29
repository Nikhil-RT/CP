# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

l = [0,1,2,3,4,5,6,7,8,9]
L = []

def isproperty309():
	# Your code goes here
	cnt = 0
	for i in range(309,8000):
		a = pow(i,5)
		a = str(a)

		for j in l:	
			if str(j) in a:
				cnt = cnt+1
		if cnt == 10:
			L.append(i)
		cnt = 0

def nthwithproperty309(n):
	isproperty309()
	return L[n]