# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
    	

	if n < 0:
		k = -len(s)
		if k > (-n):
			x = k + n
			return s[x:]+s[:x]
		x = k + n
		y = k + x
		return s[y:] + s[:y]
	return s

	if n > 0:
		
		k = len(s)

		if k < n:
			x = n - k
			return s[x:] + s[:x]
		return s[n:] + s[:n]
	
	return s