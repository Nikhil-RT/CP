# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	# return 0
	mul = -1 if n<0 else 1
	n = list(str(abs(n)))
	n = n[::-1]
	# mul = 
	# if(n%10 == 0):
	if (len(n)<=k):
    		n.append(str(d))
	else:
		n[k] = str(d)
	n = int("".join(n[::-1]))*mul
	return n

