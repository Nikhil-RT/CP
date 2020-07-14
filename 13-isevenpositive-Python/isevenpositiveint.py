# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

import pytest
import os
import sys
sys.path.append(os.getcwd())
def isevenpositiveint(x):
	# your code goes here
	# type(x)
	if (isinstance(x,int)):
		if (x>0 and x%2 ==0):
			return True
	return False

if __name__ == '__main__':
    	
	@pytest.mark.parametrize('x, check', [
    	(1, False),
    	(-1, False),
    	(-2, False),
    	(-3, False),
    	(2, True),
    	(3, False),
    	(1.0, False),
    	("yikes!", False),
    	(None, False),
    	((12), False),
    	([12], False),
    	(123456, True)
	])
	def test_isevenpositiveint(x, check):
    		assert isevenpositiveint(x) == check
	print(isevenpositiveint(12))
	print(isinstance((12),tuple))