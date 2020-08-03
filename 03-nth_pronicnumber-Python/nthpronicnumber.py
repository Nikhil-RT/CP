# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def isPronic(n):
	for i in range(n):
		p = i*(i+1)
		if p == n:
			return True
	return False

def nthpronicnumber(n):
	# Your code goes here
	lst = []
	for i in range(l3n(lst)):
		if isPronic(i):
			lst.append(i)
	return lst[n]
	pass