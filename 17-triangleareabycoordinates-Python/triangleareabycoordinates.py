# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
import math

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	s1 = math.sqrt((x1-x2)**2+(y1-y2)**2)
	s2 = math.sqrt((x2-x3)**2+(y2-y3)**2)
	s3 = math.sqrt((x3-x1)**2+(y3-y1)**2)
	s = float((s1+s2+s3)/2)
	area = float(math.sqrt(s*(s-s1)*(s-s2)*(s-s3)))
	return area