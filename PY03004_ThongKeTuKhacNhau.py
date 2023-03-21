import re
import functools
m={}
def cmp(a,b):
    if m[a]==m[b]:
        if a<b: return -1
        else : return 1
    else :
        if m[a]>m[b]: return -1
        else: return 1
n=int(input())

for i in range(n):
    s = input().lower()
    a = re.findall('[\w]+',s)
    for i in a:
        if i in m:
            m[i]=m[i]+1
        else:
            m[i]=1
a = sorted(list(m),key=functools.cmp_to_key(cmp))
for i in a:
    print(i,m[i])