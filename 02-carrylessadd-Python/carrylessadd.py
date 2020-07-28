# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.
import math

def fun_carrylessadd(x, y):
	sum = 0
	if x==0: return y
	if y==0: return x
	m = 1
	each = 0
	while(x or y):
		each = ((x%10)+(y%10))%10
		sum += each*m
		x = math.floor(x/10)
		y = math.floor(y/10)
		m = m*10
	se = str(sum)
	se.strip("0")
	return int(se)


