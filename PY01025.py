s = input()[::-1]
ans = ""
d = 0
for i in range(len(s)):
    ans = ans + s[i]
    d = d + 1
    if d==3:
        ans = ans + ','
        d=0
ans = ans[::-1]
if ans[0]==',':
    ans = ans[1::]
print(ans)