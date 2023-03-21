n = int(input())
a = []
s = 0 
for i in range(n):
    b=[int(x) for x in input().split()]
    s= s + sum(b)
    a.append(sum(b))


if n==2:
    for i in a:
        print(i//2,end=' ')
else:
    s = int(s/2/(n-1))
    for i in a:
        print((i-s)//(n-2),end=' ')
        