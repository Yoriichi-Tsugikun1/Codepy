import functools
class ThongTin:
    def __init__(self,i,name,lt,th):
        self.ma = 'TS0' + '{:d}'.format(i)
        self.name = name
        self.lt = lt
        self.th = th
        if self.lt > 10.0 : self.lt = self.lt/10
        if self.th>10.0 : self.th=self.th/10

        self.tb = (self.lt+self.th)/2

        if self.tb >= 9.5 : self.l = 'XUAT SAC'
        elif self.tb>=8: self.l = 'DAT'
        elif self.tb>=5: self.l = 'CAN NHAC'
        else: self.l='TRUOT'''
        

    def __str__(self):
        return self.ma + ' ' + self.name + ' ' + '{:.2f}'.format(self.tb) + ' ' + self.l
def cmp(a,b):
    if a.tb > b.tb : return -1
    return 1
lst = []
n = int(input())
for i in range(1,n+1):
    a = ThongTin(i,input(),float(input()),float(input()))
    lst.append(a)
lst = sorted(lst,key=functools.cmp_to_key(cmp))
for i in lst:
    print(i)