import math
def nt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

for _ in range(int(input())):
    a = input()
    if nt(int(a[:3:]))==True and nt(int(a[-3::]))==True:
        print("YES")
    else:
        print("NO")