# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	n = str(n)
	if(len(n) == 1):
		return int(n)
	elif(len(n)==2):	
		# return n
		if(int(n[0]) <= int(n[1])):
			return int(n[0])
		else:
			return int(n[1])
	else:
		count = 0
		i = -1
		for a in range(len(n)-1):
			if(int(n[i]) == int(n[i+1])):
				i = n[i]
				count = count + 1
		if (count > 0):
			return int(i)