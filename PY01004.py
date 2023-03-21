import math

def ngto(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    d = int(0)
    for j in range(1,n):
        if math.gcd(j, n)==1: d=d+1
    if ngto(d)==True: print("YES")
    else : print("NO")