import math
def ntcn(n,a):
    if math.gcd(n, a) ==1 : return True
    return False
t = int(input())
for _ in range(t):
    a = input()
    n = a[::-1]
    if ntcn(int(n), int(a))==True:
        print("YES")
    else :
        print("NO")