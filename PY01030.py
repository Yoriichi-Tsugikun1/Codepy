import math
def ntcn(n,a):
    if math.gcd(n, a) ==1 : return True
    return False
a,n = [int(x) for x in input().split()]
d = 0
for i in range(10**(n-1),10**(n)):
    if ntcn(i,a)==True:
        if d == 10:
            print()
            d=0
        d=d+1
        print(i,end=' ')