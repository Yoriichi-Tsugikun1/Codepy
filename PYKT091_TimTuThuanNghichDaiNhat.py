import re
file = open("VANBAN.in", "r")
m={}
ans = 0
for i in file:
    if i[-1]=='\n':
        i = i[:-1]
    a = re.split('\s+',i)
    for j in a:
        if j == j[::-1]:
            if j in m:
                m[j]=m[j]+1
                ans = max(ans,len(j))
            else:
                m[j]=1
                ans = max(ans,len(j))
file.close()
for i in m:
    if len(i)==ans:
        print(i,m[i])