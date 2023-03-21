import sys
a = [0]*505
a[0]=1
a[1]=1
for i in range(2,505):
    if a[i]==0:
        for j in range(2*i,505,i):
            a[j]=1

t = int(input())
for i in range(t):
    n = input()
    if a[len(n)]==0:
        d = 0
        for j in n:
            if a[int(j)]==0: d=d+1
        
        if d > len(n)-d: print("YES")
        else: print("NO")
    else: print("NO")