# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math
def isKaprekar(n):
    if n<= 0:
        return False
    k = n**2
    if k < 10:
        if k == n :
            return True
    num = math.ceil(math.log(k,10))
    count = 1

    while count < num:
        if k%10**count == 0:
            count +=1
            continue
        if (k%10**count) + (kW//10**count) == n:
            return True
            break
        count += 1
    return False

    
def fun_nth_kaprekarnumber(n):
    lst = []
    for i in range(80000):
        if isKaprekar(i):
            lst.append(i)
    return lst[n];