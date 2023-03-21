import functools
h,b = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]

m = {}

for i in a:

    if i not in m:
        m[i] = 1
    else:
        m[i] += 1
def cmp(i1,i2):
    if  m[i1]==m[i2]:
        if i1>i2: return 1
        else: return -1
    elif m[i1]>m[i2]: return -1
    else: return 1

a = sorted(list(m),key=functools.cmp_to_key(cmp))

if m[a[0]] == m[a[-1]]:
    print("NONE")
else:
    maxx = m[a[0]]
    for i in a:
        if m[i]!=maxx:
            print(i)
            break