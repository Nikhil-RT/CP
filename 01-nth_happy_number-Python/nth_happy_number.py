# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def sum(n):
	a = 0
	while n > 0:
		r = n%10
		a += r**2
		n//=10
	return a

def ishappynumber(n):
	lst = []
	while (sum(n) not in lst):
		# res = sum(n)
		if (sum(n) == 1):
			return True
		else:
			lst.append(sum(n))
			n = sum(n)
	return False

def fun_nth_happy_number(n):
	a = []
	for j in range(40):
		if (ishappynumber(j)):
			a.append(j)
	return a[n]