# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
from math import isclose
import math

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = math.sqrt((x1-x2)**2+(y1-y2)**2)
	b = math.sqrt((x2-x3)**2+(y2-y3)**2)
	c = math.sqrt((x3-x1)**2+(y3-y1)**2)
	if (isclose(a**2+b**2, c**2, rel_tol=1e-9, abs_tol=0.0) or isclose(a**2+c**2, b**2, rel_tol=1e-9, abs_tol=0.0) or isclose(b**2+c**2, a**2, rel_tol=1e-9, abs_tol=0.0)):
		return True
	return False
