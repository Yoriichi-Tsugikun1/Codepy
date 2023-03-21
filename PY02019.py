import math
def ntcn(n,k):
    if math.gcd(n, k)==1:
        return True
    return False


n = int(input())

a = [int(x) for x in input().split()]

a = sorted(a)

for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if ntcn(a[i],a[j])==True:
            print(a[i],a[j])