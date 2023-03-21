a=[]
b=[0]*(10**6+5)
b[0]=1
b[1]=1
for i in range(2,10**6+5):
    if b[i]==0:
        for j in range(2*i,10**6+5,i):
            b[j]=1
        
        a.append(i)
x,y = [int(x) for x in input().split()]
print(y,end=' ')
for i in range(x):
    y=y+a[i]
    print(y,end=' ')