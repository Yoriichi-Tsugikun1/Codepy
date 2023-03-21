b = [0]*(2*10**6+5)
b[0]=1
b[1]=1
for i in range(2,2*10**6+5):
    if b[i]==0:
        for j in range(2*i,2*10**6+5,i):
            b[j]=i
        b[i]=i
s=0
for _ in range(int(input())):
    a = int(input())
    while(a>1):
        s=s+int(b[a])
        a=a//b[a]

print(s)