def BFS(st,ke,check):
    q = [st]
    check[st]=1
    while len(q) > 0:
        x = q.pop()
        for i in ke[x]:
            if check[i]==0:
                check[i]=1
                q.append(i)
for _ in range(int(input())):
    n,m = [int(x) for x in input().split()]
    ke = []
    for i in range(1,n+2):
        ke.append([])
    for i in range(m):
        x,y = [int(j) for j in input().split()]
        ke[x].append(y)
        ke[y].append(x)
    lt= 0 
    check=[0]*(n+1)
    for i in range(1,n+1):
        if check[i]==0:
            lt = lt + 1
            BFS(i,ke,check)

    ans1 = 0
    for i in range(1,n+1):
        d = 0
        check=[0]*(n+1)
        check[i]=1
        for j in range(1,n+1):
            if check[j]==0:
                BFS(j,ke,check)
                d = d + 1
        
        if d > lt :
            lt= d
            ans1 = i
    print(ans1)