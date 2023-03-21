a = []
while True:
    try:
        a = a + [int(x) for x in input().split()]
    except EOFError:
        break
t = a[0]
d = 1
for _ in range(t):
    n = a[d] 
    d = d + 1
    m = a[d]
    d = d + 1
    mt = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(a[d])
            d = d + 1
        mt.append(b)
    for i in range(n):
        for j in range(n):
            ans = 0
            for k in range(m):
                ans = ans + mt[i][k] * mt[j][k]
            print(ans,end=' ')
        print()
