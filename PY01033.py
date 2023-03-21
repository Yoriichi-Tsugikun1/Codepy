import math
def nt(a,n,k):
    if math.gcd(a, n) == 1 and math.gcd(a, k)==1 and math.gcd(n, k)==1 : 
        return True
    return False
a,k = [int(x) for x in input().split()]
for i in range(a,k+1):
    for j in range(i+1,k+1):
        for k in range(j+1,k+1):
            if nt(i, j, k)==True:
                a = '(' + str(i)+ ', ' + str(j) + ', ' + str(k) + ')' 
                print(a)