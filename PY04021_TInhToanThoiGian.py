import functools
class ThongTin:
    def __init__(self,ma,name,bd,kt):
        self.ma = ma
        self.name=name
        self.bd = bd
        self.kt = kt

        a,b = [int(x) for x in bd.split(':')]
        c,d = [int(x) for x in kt.split(':')]
        time = c*60+d-a*60-b
        self.gio = time//60
        self.phut = time%60
    def __str__(self):
        return (self.ma + ' ' + self.name + ' ' + str(self.gio) + ' gio ' + str(self.phut) + ' phut')
def cmp(a,b):
    if a.gio == b.gio:
        if a.phut > b.phut:
            return -1
        return 1
    elif a.gio>b.gio:
        return -1
    else:
        return 1
lst = []
n = int(input())
for _ in range(n):
    a = ThongTin(input(),input(),input(),input())
    lst.append(a)
lst = sorted(lst,key = functools.cmp_to_key(cmp))
for i in lst:
    print(i)