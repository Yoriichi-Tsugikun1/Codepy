n,m = [int(x) for x in input().split()]
a = []*(n+1)

for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
if n==m:
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=" ")
        print()

elif n>m:
    
    d = n
    for i in range(n):
        if i%2==0 and d!=m:
            d=d-1
            continue
        else:
            for j in range(m):
                print(a[i][j],end=" ")
            print() 
else:
    
    for i in range(n):
        d=m
        for j in range(m):
            if j%2==1 and d!=n:
                d = d-1
                continue
            else:
                print(a[i][j],end=' ')
        print()
            