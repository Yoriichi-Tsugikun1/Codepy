s = input()
k = int(input())
if len(s)%2==1:
    s = s[:len(s)-1]
m={}
for i in range(0,len(s),2):
    id = int(s[i]+s[i+1])
    if id in m:
        m[id]=m[id]+1
    else:
        m[id]=1
kt = 0
a = sorted(m)
for i in a:
    if m[i]>=k:
        print(i,m[i])
        kt = 1
if kt==0:
    print("NOT FOUND")