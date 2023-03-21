a=[0]*(10**6+5)

a[0]=1
a[1]=1
for i in range(2,10**6+5):
    if a[i]==0:
        for j in range(2*i,10**6+5,i):
            a[j]=1
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(13,n):
        if a[i]==0 :
            m = int(str(i)[::-1])
            if a[m]==0 and m!=i and m<n and i<m:
                print(i,m,end=' ')
    print()