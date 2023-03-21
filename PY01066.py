import math
t = int(input())
for _ in range(t):
    s=input()
    m=s[::-1]
    kt = int(0)
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(m[i])-ord(m[i-1])):
            print("NO")
            kt=int(1)
            break
    if kt==0:
        print("YES")