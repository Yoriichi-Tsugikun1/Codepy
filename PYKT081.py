import re
def check(s):
    if s[-1]=='.': return False
    for i in s:
        if i!='.' and (i<'0' or i >'9'): return False
    a=str(s).split('.')
    if len(a)!= 4 : return False
    for i in a:
        if int(i)>255:
            return False
    return True
t = int(input())
for _ in range(t):
    s = input().strip()
    if check(s)==True:
        print("YES")
    else:
        print("NO")
