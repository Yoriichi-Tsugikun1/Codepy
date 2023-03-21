import math

a,b,c,d = [int(x) for x in input().split()]

tu = a * d  + b * c
mau = b*d

ucln = math.gcd(tu,mau)

print(str(int(tu/ucln))+"/"+str(int(mau/ucln)))