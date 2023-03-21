n = int(input())
a = []

for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)

dl = int(input())

s1 = 0
s2 = 0
for i in range(n):
    for j in range(n):
        if i==j : continue
        elif j>i: s1 = s1 + a[i][j]
        else : s2 = s2 +a[i][j]

if abs(s1-s2)<=dl:
    print("YES")
else:
    print("NO")
print(abs(s1-s2))