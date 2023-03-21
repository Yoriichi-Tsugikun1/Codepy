n = int(input())

a = [int(x) for x in input().split()]

ans = 10**9
index  = 0

for i in a:
    s = 0 
    for j in a :
        s = s + abs(i-j)
    if s < ans :
        ans = s
        index = i

print(ans,index)