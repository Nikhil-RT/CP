# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def isTidy(n):
    a = 10
    while n > 0:
        num = n%10 
        n //= 10
        if num > a:
            return False
        a = num
    return True

def fun_nth_tidynumber(n):
    lst = []
    i = 1
    while(len(lst) <= n):
        if isTidy(i):
            lst.append(i)
        i += 1
    return lst[n]