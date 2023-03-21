a,b=[int(x) for x in input().split()]

s = [int(x) for x in input().split()]
s=sorted(s)
d=1
for i in range(1,len(s)):
    if abs(s[i]-s[i-1])>b:
        d=d+1
print(d)