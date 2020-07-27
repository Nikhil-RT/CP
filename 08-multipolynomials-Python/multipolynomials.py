# Background: we can represent a polynomial as a list of its coefficients. For example, [2, 3, 0, 4] could represent 
# the polynomial 2x3 + 3x2 + 4. With this in mind, write the function multiplyPolynomials(p1, p2) which takes two 
# lists representing polynomials as just described, and returns a third list representing the polynomial which is 
# the product of the two. For example, multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 
# 5), and:    (2x**2 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns the list [8, 10, 12, 15].

def multipolynomials(p1, p2):
	# Your code goes here
	ls = [0]*(len(p1)+len(p2)-1)
	for i in range(len(p1)):
		f = len(p1)-(i+1)
		for j in range(len(p2)):
			l = len(p2)-(j+1)
			ls[len(ls)-(f+l+1)] += p1[i]*p2[j]
	
	return 0

