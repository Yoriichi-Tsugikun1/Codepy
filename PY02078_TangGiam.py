t = int(input())
for _ in range(t):
    n = int(input())

    a , b = [0]*(n+1), [0]*(n+1)

    f = [1]*(n+1)

    for i in range(n):
        a[i] , b[i] = [float(x) for x in input().split()]
    
    ans = 1
    
    for i in range(n):
        for j in range(0,i):
            if a[i]>a[j] and b[i]<b[j]:
                f[i] = max(f[i],f[j]+1)
        ans = max (ans,f[i])
    print(ans)