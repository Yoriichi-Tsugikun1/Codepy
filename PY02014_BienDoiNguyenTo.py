b = []
nt = [0]*10001
nt[0]=1
nt[1]=1

for i in range(2,10001):
    if nt[i]==0:
        for j in range(2*i,10001,i):
            nt[j]=1
        b.append(i)
n = int(input())
a = [int(x) for x in input().split()]
ans = 0
for i in a:
    minn = 10**9
    for j in b:
        minn = min(minn,abs(i-j))
    ans = max(ans,minn)
print(ans)