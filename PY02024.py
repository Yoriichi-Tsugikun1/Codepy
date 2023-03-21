import functools

def tich(n):
    t=1
    while n!=0:
        t=t*(n%10)
        n=int(n/10)
    
    return t

def cmp(a,b):
    if tich(a)==tich(b):
        if a > b :
            return 1
        else:
            return -1
    if tich(a)<tich(b):
        return -1
    else :
        return 1

t = int(input())
for _ in range(t):
    d = int(input())
    a=[int(x) for x in input().split()]
    a=sorted(a,key=functools.cmp_to_key(cmp))
    for i in a:
        print(i,end=' ')
    print()