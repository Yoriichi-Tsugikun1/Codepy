a,k,n = [int(x) for x in input().split()]

if k > a :
    c = 1
    ans = k - a
    for i in range(ans,n-a+1,k):
        c=0
        print(i,end=' ')
    if c==1: print("-1")
else:
    ans = 0
    for i in range(1,n-a+1):
        if (a + i)%k==0:
           ans = i
           break
    if ans == 0: print("-1")
    else :
        c=1
        for i in range(ans,n-a+1,k):
            c=0
            print(i,end=' ')
        if c == 1 : print("-1")