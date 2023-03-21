import re
import functools
m={}
def cmp(a,b):
    if m[a]==m[b]:
        if a<b : return -1
        else: return 1

    if m[a]>m[b]:
        return -1
    else :
        return 1
n , k = [int(x) for x in input().split()]

for i in range(n):
    s = input().lower()
    a = re.findall('[\w]+',s)
    for i in a:
        if i in m:
            m[i] += 1
        else :
            m[i] = 1
a = sorted(m.keys(), key=functools.cmp_to_key(cmp))
for i in a :
    if m[i]<k:
        break
    else:
        print(i,m[i])