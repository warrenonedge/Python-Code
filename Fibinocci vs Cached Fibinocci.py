def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
import sys
lstFib = [0]*(1000000000)
def cacheFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if lstFib[n]!=0:
        return lstFib[n]
    lstFib[n] = cacheFib(n-1)+cacheFib(n-2)
    return lstFib[n]

##for x in xrange(sys.maxint/10-1):
##    print(cacheFib(x))

cacheFib(1000000000-1)