for _ in range(int(input())):
    n = int(input())
    b={}
    for i in map(int,input().split()):
        if i in b:
            b[i]=b[i]+1
        else:
            b[i]=1
    a=list(b)
    a = sorted(a,key = lambda x : b[x])
    ans = b[a[-1]]
    if ans > n//2:
        print(a[-1])
    else :
        print("NO")
    '''
    s = 0
    ans = 0
    for i in b:
        if s < b[i]:
            s=b[i]
            ans = i
    if s > n//2:
        print(ans)
    else:
        print("NO")'''