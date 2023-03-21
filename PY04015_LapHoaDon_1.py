import functools
class ThongTin:
    def __init__(self,i,name,csc,csm):
        self.ma = 'KH'+'{:02d}'.format(i)
        self.name= name
        self.csm = csm
        self.csc = csc

        s = csm-csc
        if s <= 50:
            s *= 100
            s += s * 0.02
        elif s <= 100:
            s = 50 * 100 + (s - 50) * 150
            s += s * 0.03
        else:
            s = 50 * 100 + 50 * 150 + (s - 100) * 200
            s += s * 0.05
        self.tra = round(s)
    def __str__(self):
        return self.ma + ' ' + self.name + ' ' + str(self.tra)
def cmp(a,b):
    if a.tra > b.tra :
        return -1
    return 1
n = int(input())
lst = []
for i in range(1,n+1):
    a = ThongTin(i,input(),int(input()),int(input()))
    lst.append(a)
lst = sorted(lst,key=functools.cmp_to_key(cmp))
for i in lst:
    print(i)