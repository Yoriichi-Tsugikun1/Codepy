import re
import functools
m={}
def cmp(a,b):
    if m[a]==m[b]:
        if a<b: return -1
        else: return 1
    if m[a]>m[b]: return -1
    else: return 1

n = int(input())

for i in range(n):
    s = input().lower()
    a = re.findall('[\w]+',s)
    for j in a:
        ans = re.split('\d+',j)
        for k in ans:
            if k!='':
                if k in m:
                    m[k]=m[k]+1
                else:
                    m[k]=1
            else:
                continue    

a = sorted(m.keys(),key=functools.cmp_to_key(cmp))
for i in a:
    print(i,m[i])
