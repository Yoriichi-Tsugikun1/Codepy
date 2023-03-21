s = input()

if len(s)%2==1: 
    s = s[:len(s)-1]

m={}
for i in range(0,len(s),2):
    id = int(s[i]+s[i+1])
    if id in m :
        m[id]=m[id]+1
    else:
        m[id]=1
for i in m :
    print(i,m[i])