import math
def tn(n):
    l=int(0)
    r=int(len(n)-1)
    if len(n)%2!=0: return False
    while l<r:
        if n[l]!=n[r] : return False
        l=l+1
        r=r-1
    return True
t=int(input())
for i in range((t)):
    a = []
    a.append('2')
    a.append('4')
    a.append('6')
    a.append('8')
    kq = []
    n=int(input())
    while True:
        m = a.pop(0)
        if int(m)>=n: break
        else:
            if tn(m)==True:
                kq.append(m)
        a.append(m+'0')
        a.append(m+'2')
        a.append(m+'4')
        a.append(m+'6')
        a.append(m+'8')
    for i in kq:
        print(i,end=" ")
    print()