a,k,n = [int(x) for x in input().split()]

ans = (int(a/k) + 1 )*k

c = 1 
for i in range(ans,n+1,k):
    c=0
    print(i-a,end=' ')
if c == 1 : print("-1")