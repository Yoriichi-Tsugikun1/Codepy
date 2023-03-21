nt = [0]*(10**6+5)
nt[0]=1
nt[1]=1
for i in range(2,10**6+5):
    if nt[i]==0:
        for j in range(2*i,10**6+5,i):
            nt[j]=1

n = int(input())
a=[]
m={}
for i in map(int,input().split()):
    if nt[i]==0:
        if i in a:
            m[i]=m[i]+1
        else:
            a.append(i)
            m[i]=1
for i in a:
    print(i,m[i])