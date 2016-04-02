for i in xrange(int(raw_input())):
    N = int(raw_input())
    l = [100]
   # print N
    p=0
    for j in xrange(N):
        p = int(raw_input())
     #   print j,p
        l.append(p)
    M = 0
    jp =  1
    for jp in xrange(N):
        if l[jp-1] == jp:
            M = 1
            print jp

    if M != 1:
        print "Not Found"

