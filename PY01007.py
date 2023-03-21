import math

t = int(input())
for i in range(t):
    n,x,m = [float(x) for x in input().split()]
    d = int(0)
    while n<m:
        d=d+1
        n=n+n*x/100
    print(d)