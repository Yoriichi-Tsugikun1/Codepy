t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    l,r = [0]*n,[0]*n
    l[0],r[-1]=a[0],a[-1]
    minn = a[-1]
    cnt = 0 
    for i in range(1,n):
        l[i]=max(l[i-1],a[i])
    for i in range(n-2,-1,-1):
        if a[i]==a[i+1]:
            r[i]=-1
        else :
            r[i]=min(minn,a[i])
            minn = r[i]
    for i in range(n):
        if l[i]==r[i] : cnt = cnt + 1
    print(cnt)