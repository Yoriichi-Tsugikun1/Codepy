import math
t = int(input())
for _ in range(t):
    s = input()
    n = s[::-1]
    c = 0
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(n[i])-ord(n[i-1])):
            c=1
            break
    if c==0: print("YES")
    else: print("NO")
