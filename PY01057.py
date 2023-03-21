nt=[0]*(505)
nt[0]=1
nt[1]=1
for i in range(2,505):
    if nt[i]==0:
        for j in range(2*i,505,i):
            nt[j]=1

for _ in range(int(input())):
    s = input()
    c=1
    d=0
    for i in range(len(s)):
        if (nt[i]==0 and nt[int(s[i])]==1) or (nt[i]==1 and nt[int(s[i])]==0):
            c=0
            break
    if c==0:
        print("NO")
    else:
        print("YES")