import math
F=[0]*93
F[0]=0
F[1]=1
F[2]=1
for i in range(3,93):
    F[i]=F[i-2]+F[i-1]
for _ in range(int(input())):
    a,b=[int(x) for x in input().split()]
    for i in range(a,b+1):
        print(F[i],end=' ')
    print()