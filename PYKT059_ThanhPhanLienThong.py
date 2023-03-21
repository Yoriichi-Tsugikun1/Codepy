
def BFS(n,ke,st):
    q = [st]
    check = [0]*(n+1)
    check[st]=1
    while len(q)>0:
        x = q.pop()
        for i in ke[x]:
            if check[i]==0:
                check[i]=1
                q.append(i)
    kt = 0
    for i in range(1,n+1):
        if check[i]==0:
            print(i)
            kt=1
    if kt==0:
        print(0)
n,m,st = [int(x) for x in input().split()]
ke = []
for i in range(1,n+2): ke.append([])
for i in range(m):
    x,y = [int(j) for j in input().split()]
    ke[x].append(y)
    ke[y].append(x)
BFS(n,ke,st)