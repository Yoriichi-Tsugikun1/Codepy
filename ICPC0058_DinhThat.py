def BFS(st,end,l,n,dt):
    check = [0]*(n+1)
    q = [st]
    while len(q)>0:
        s = q.pop()
        if s==end :
            return False
        for i in l[s]:
            if check[i]==0 and i != dt:
                check[i] = 1
                q.append(i)
    
    return True

for _ in range(int(input())):
    n,m,st,end=[int(x) for x in input().split()]
    l=[]
    for i in range(n+1):
        l.append([])
    for i in range(m):
        x,y = [int(h) for h in input().split()]
        l[x].append(y)
    cnt = 0
    for i in range(1,n+1):
        if i==st or i==end:
            continue
        if BFS(st,end,l,n,i)==True: cnt = cnt+1

    print(cnt)