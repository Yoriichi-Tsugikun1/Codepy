n = int (input())
a = []
for i in range(n):
    a.append(input())
s = a[0]
m,check,ans = len(s),0,10**9
for i in range(m):
    d = 0
    for j in range(n):
        x = a[j]
        for k in range(m):
            if x == s:
                
                break
            x = x[1::]+x[0]
            d = d +1 
        if x !=s:
            check = 1
            break
    ans = min(ans,d)
    s = s[1::]+s[0]
if check==1:
    print("-1")
else:
    print(ans)