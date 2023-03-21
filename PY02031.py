nt =[1]*1005
nt[0]=0
nt[1]=0
for i in range(2,1005):
    if nt[i]==1:
        for j in range(2*i,1005,i):
            nt[j]=0
a,b = [int(x) for x in input().split()]

mt = []
for i in range(a):
    h = [int(x) for x in input().split()]
    mt.append(h)

for i in range(a):
    for j in range(b):
        mt[i][j] = nt[mt[i][j]]
for i in mt:
    print(*i)
