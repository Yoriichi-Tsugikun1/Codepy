n = int(input())
a = []

while True:
    a = a + [int(x) for x in input().split()]
    if len(a)==n:
        break

c = []
l = []
for i in a :
    if i%2==0: c.append(i)
    else : l.append(i)
c = sorted(c)
l = sorted(l,reverse=True)
d1 = 0
d2 = 0
for i in range(n):
    if a[i]%2==0:
        print(c[d1],end=' ')
        d1 = d1 + 1
    else :
        print(l[d2],end=' ')
        d2 = d2 + 1