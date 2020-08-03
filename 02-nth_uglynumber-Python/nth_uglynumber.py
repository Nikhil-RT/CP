# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

def prime_factors(n):
    lst = []
    m = n
    while n%2 == 0:
        lst.append(2)
        n //= 2
    for i in range(3,n,2):
        while n%i == 0:
            lst.append(i)
            n //= i
    if n > 2:
        lst.append(n)
    return lst

def isUgly(n):
    l = prime_factors(n)
    for i in l:
        if i!=2  and i!=3 and i!=5:
            return False
    return True 

def fun_nth_uglynumber(n):
    lst = [1]
    i = 2
    while (len(lst) <= n+1):
        if isUgly(i):
            lst.append(i)
        i += 1
    return lst
