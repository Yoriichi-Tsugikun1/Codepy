def KT(s,n,a,b,c):
    if len(s)==n and c>=b and b>=a and a>0:
        print(s)
    if len(s)<n:
        KT(s+'A',n,a+1,b,c)
        KT(s+'B',n,a,b+1,c)
        KT(s+'C',n,a,b,c+1)

n = int((input()))
for i in range(3,n+1):
    KT('',i,0,0,0)