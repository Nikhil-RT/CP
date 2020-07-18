# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	abc = str(n)
	if(len(abc) == 1):
		return int(n)
	elif(len(abc) == 2):	
		# return n
		if(int(abc[0]) <= int(abc[1])):
			return int(abc[0])
		else:
			return int(abc[1])
	else:
		count = 0
		i = -1
		for a in range(len(n)-1):
			if(int(abc[i]) == int(abc[i+1])):
				i = abc[i]
				count = count + 1
		if (count > 0):
			return int(i)