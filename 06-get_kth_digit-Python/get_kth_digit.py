# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	digit = str(digit)
	digit = digit[::-1]
	if(k > 2):
    		return 0
	for i in range(len(digit)):
    		# print(int(digit[k]))
    		return int(digit[k])
	return 0

if __name__ == '__main__':
    	# print(digit)
    	print(fun_get_kth_digit(789,3))
	