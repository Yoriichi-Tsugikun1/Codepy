b = ['2','3','5','7']

n = 0 
c = []
def kt(s):
    if s[-1]=='2' : return False
    a =set(list(s)) 
    if len(a)!=4 : return False
    return True

def Try(k,s):
    if k>=4:
        if kt(s)==True:
            c.append(s)
    if k==n : return
    for i in range(4):
        Try(k+1,s+b[i])

n = int(input())
Try(0,'')
c = sorted(c,key=lambda x: len(x))
for i in c:
    print(i)