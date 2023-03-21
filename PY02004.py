t = int(input())
a = [int(x) for x in input().split()]
d=0
for i in range(1,len(a)):
    if a[i]!=a[i-1]:
        d=d+1
print(d)