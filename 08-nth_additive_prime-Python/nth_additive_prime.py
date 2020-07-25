# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def is_prime(m):
	if m <= 1:
		return False
	for i in range(2,m):
		if m%i == 0:
			return False
	return True

def fun_nth_additive_prime(n):
	if n == 0:
		return 2
	m = 3
	x = 0
	y = 0	
	lst = []
	
	while len(lst)!=n:
		if isprime(m):
			x = list(str(m))
			y = sum(map(int,x))
			if is_prime(y):
				lst.append(m)
		m = m + 1
	return lst[n-1]