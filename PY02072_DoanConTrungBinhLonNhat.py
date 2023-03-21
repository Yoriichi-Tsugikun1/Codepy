n = int(input())

a = [int(x) for x in input().split()] + [0]

maxx = max(a)

ans ,d = 0,0
for i in a:
    if i == maxx:
        d = d + 1 
    else:
        ans = max(ans,d)
        d=0
print(ans)