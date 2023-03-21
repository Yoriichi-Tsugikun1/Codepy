n = int(input())
a = [float(x) for x in input().split()]
s = 0
d = 0
a = sorted(a)
x=a[0]
y=a[-1]
for i in range(1,len(a)-1):
    if a[i]==x or a[i]==y : continue
    else:
        s=s+a[i]
        d=d+1

ans = s/d
print("{:.2f}".format(ans))