# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	if len(a) == 0: 
		return True
	b = max(a)
	c = 0
	if a[0] == b:
		for i in range(len(a)):
			if i == len(a)-1:
				break
			if a[i] >= a[i+1]:
				c = c + 1

	else:
		for i in range(len(a)):
			if len(a) - 1 == i:
				break
			if a[i+1] >= a[i]:
				c = c + 1

	return c == len(a)-1