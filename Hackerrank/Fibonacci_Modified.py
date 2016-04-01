a,b,c = raw_input().split( )
a = int(a)
b = int(b)
c = int(c)
i=2
N =0
while (c > i) :
   N = b*b + a
   a = b
   b = N
   i = i+1
print N


