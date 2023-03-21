import math
def nto(n):
    if n < 2 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
def ti(n):
    s=int(0)
    while (n>0):
        k = n%10
        if nto(int(k))==False: return False
        s = s + k
        n = int(n/10)
    if nto(s)== False: return False
    return True
    
t = int(input())
for _ in range(t):
    n = int(input())
    if nto(n)==True and nto(int(str(n)[::-1]))==True and ti(n)==True: print("Yes")
    else : print("No")