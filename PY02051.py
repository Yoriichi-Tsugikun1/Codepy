import math
a,b=[int(x) for x in input().split()]
ucln = int(math.gcd(a,b))
print(str(int(a/ucln)) + "/" + str(int(b/ucln)))