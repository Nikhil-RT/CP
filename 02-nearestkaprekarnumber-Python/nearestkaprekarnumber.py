# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math
def isKaprekar(n):
    if n <= 0:
        return False
    k = n**2
    if k < 10:
        if k == n:
            return True
    num = math.ceil(math.log(k,10))
    count = 1
    while count < num:
        if k%10**count == 0:
            count += 1
            continue
        if k%10**count + k//10**count == n:
            return True
            break
        count += 1
    return False

def fun_nearestkaprekarnumber(n):
    l = n - math.floor(n)
    h = math.ceil(n) - n
    if isKaprekar(n):
        return n

    while(True):
        if isKaprekar(n - l):
            if isKaprekar(n + h):
                if h < l:
                    return n+h
                    break
                else:
                    return n-l
                    break
            else:
                return n-l
                break
        if isKaprekar(n+h):
            return n+h
            break
        # n+h = 1