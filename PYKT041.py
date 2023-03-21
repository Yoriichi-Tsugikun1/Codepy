a=[]
n=int(input())
for i in range(n):
    a.append(input())
dn=[0]*n
dd=[0]*n
for i in range(n):
    for j in range(n):
        if a[i][j]=='C':
            dn[i]=dn[i]+1
            dd[j]=dd[j]+1

s = 0
for i in range(n):
    s = s + (dn[i]*(dn[i]-2+1))/2
    s = s + (dd[i]*(dd[i]-2+1))/2
print(int(s))    