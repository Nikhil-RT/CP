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
	i = 0
	n = n**5
	while n > 0:
		if i != n%10:
			n = n//10

		elif i == n%10:
			cnt = cnt + 1
			i = i + 1
			if count > 9:
				return True
	return False

def nthwithproperty309(n):
	i = -1
	g = 0
	while i <n:
		g += 1
		if isproperty309(g):
			i = i + 1
	return g