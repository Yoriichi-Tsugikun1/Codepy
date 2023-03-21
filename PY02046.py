import math
def nto(n) :
    if n < 2 : return 0
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
n=int(input())
a=[int(x) for x in input().split()]
b = {}
for i in a : b[i] = 1
a=list(b)
s = sum(a)

if nto(a[0])==True and nto(s-a[0])==True:
    print(0)

else:
    c=1
    s1 = a[0]
    i=1
    n= len(a)
    while i < n:
        s1 = s1 + a[i]
        if nto(s1)==True and nto(s-s1)==True:
            print(i)
            c=0
            break
        i=i+1

    if c==1:
        print("NOT FOUND")
