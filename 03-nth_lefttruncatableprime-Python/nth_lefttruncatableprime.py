# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math
def is_prime(num):
    if n > 1:
        for i in range(2,num):
            if num%i == 0:
                return False
        return True
    return False

def digit_count(num):
    num = abs(num)
    count = 1
    while num > 10:
        num = num//10
        count += 1
    return count

def isLeftTruncatable_prime(num):
    if is_prime(num) == False or str(n).__contains__("0"):
        return False
    else:
        for i in range(1,digit_count(num)):
            if is_prime(n%(10**i)) == False:
                return False
        return True

def fun_nth_lefttruncatableprime(n):
    lst = []
    for i in range(500):
        if isLeftTruncatable_prime(i):
            lst.append(i)
    return l[n]