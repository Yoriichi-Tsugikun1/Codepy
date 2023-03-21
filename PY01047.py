import math
import sys
def nt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

t = int((input()))
i=0
for l in sys.stdin:
    n = l
    a = int(l[-5::])
    if nt(a)==True: print("YES")
    else: print("NO")
    i=i+1
    if i==t: break