n,m = [int(x) for x in input().split()]
a = []
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
v = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(False)
    v.append(b)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
s = 0
for i in range(n):
    for j in range(m):
        if a[i][j]==-1: 
            for k in range(8):
                hx = i+dx[k]
                hy = j+dy[k]
                if hx>=0 and hx<n and hy>=0 and hy<m and v[hx][hy]==False:
                    s=s+a[hx][hy]
                    v[hx][hy]=True
print(s)