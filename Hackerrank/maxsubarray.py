T = int(raw_input())
for i in xrange(T):
    L= []
    N = int(raw_input())
    minus=0
    positive =0
    for j in xrange(N):
        P = int(raw_input())
        if P<0:
            minus = minus+1
        else:
            positive = positive+1
        L.append(P)
    if minus == N:
        df = int()
        

