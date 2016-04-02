import math
def factorialLength(n):
    count=0;
    while (n%2 == 0):
        n = n/2
        count += 1

    i = 3
    while i < math.sqrt(n):
        while n%i == 0:
            count += 1
            n = n/i
    i = i + 2

    if n > 2:
        count+=1
    return count


l = [0]*101


def factorial(n):
    if n==0 or n==1:
        l[n] = 1
        return 1
    else:
        l[n] = n * factorial(n-1)
        return l[n]


l[0] = 1
factorial(100)
for i in xrange(100):
    print l[i]
