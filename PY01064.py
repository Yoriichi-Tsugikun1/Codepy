import math
def kt(n,m):
    x = math.pow(2,n-1)
    if m==x: return n
    elif m<x : return kt(n-1,m)
    else: return kt(n-1,m-x)


for _ in range(int(input())):
    a,b=[int(x) for x in input().split()]
    print(chr(kt(a,b)+64))