a=[0]*(10**6+5)
a[0]=1
a[1]=1
for i in range(2,10**6+5):
    if a[i]==0:
        for j in range(2*i,10**6+5,i):
            a[j]=1
t = int(input())
for _ in range(t):
    n = int(input())
    s = int(0)
    for i in range(2,n-6):
        if (a[i]==0 and a[i+2]==0 and a[i+6]==0) or (a[i]==0 and a[i+4]==0 and a[i+6]==0): 
            s=s+1
    print(s)