# A happy prime is a number that is both happy and prime.
# Write the function nthHappyPrime(n) which takes a non-negative integer
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def ishappynumber(n):
	lst = []
	while(sum(n) not in lst):
		result = sum(n)
		if (result == 1):
			return True
		else:
			lst.append(result)
			n = result
	return False

	def sum(n):
		i = 0
		while(n>0):
			r = n%10
			i+=(r**2)
			n//=10
		return i

def fun_nth_happy_prime(n):
    # return 0
    a = []
    for i in range(len(a)):
        if (ishappynumber(i)):
            a.append(i)
    return a[n]
