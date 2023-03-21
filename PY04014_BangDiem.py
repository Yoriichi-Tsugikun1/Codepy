import functools
class SV:
    def __init__(self,j,name,a):
        self.tt = 'HS'+'{:02d}'.format(j)
        self.name = name
        d = 0
        d+=(a[0]+a[1])*2
        for i in range(2,10):
            d+=a[i]
        d = round(d*100+1)/(12*100)
        self.t = d
        if self.t >= 9: self.xh = "XUAT SAC"
        elif self.t >= 8 : self.xh = "GIOI"
        elif self.t >= 7 : self.xh = "KHA"
        elif self.t >= 5 : self.xh = "TB"
        else : self.xh = "YEU"
    
    def __str__(self):
        return self.tt+' '+self.name+' '+'{:.1f}'.format(self.t)+' '+self.xh
def cmp(a,b):
    if a.t>b.t: return -1
    return 1
lsv = []
for i in range(int(input())):
    s = input()
    a = [float(x) for x in input().split()]
    sv = SV(i+1,s,a)
    lsv.append(sv)
lsv = sorted(lsv,key=functools.cmp_to_key(cmp))
for i in lsv:
    print(i)