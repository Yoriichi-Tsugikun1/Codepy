nt =[0]*1005
nt[0]=1
nt[1]=1
for i in range(2,1005):
    if nt[i]==0:
        for j in range(2*i,1005,i):
            nt[j]=1

n = int(input())
a = [int(x) for x in input().split()]
b=[]
for i in a :
    if nt[i]==0:
        b.append(i)

b=sorted(b)
d = 0
for i in a:
    if nt[i]==0:
        print(b[d],end=' ')
        d=d+1
    else : print(i,end=' ')