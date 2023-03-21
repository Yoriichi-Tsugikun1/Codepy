class ThongTin:
    def __init__(self,i,name,bd,kt,lm):
        self.ma = 'T'+'{:02d}'.format(i)
        self.name=name
        self.bd = bd
        self.kt = kt
        self.lm = int(lm)

        a,b = [int(x) for x in bd.split(':')]
        c,d = [int(x) for x in kt.split(':')]

        time = c*60+d-a*60-b
        self.time = time
    def settime(self,a):
        self.time = self.time + a
    def setlm(self,a):
        self.lm = self.lm+a
    def __str__(self):
        return self.ma + ' ' + self.name +  ' ' + '{:.2f}'.format(self.lm*60/self.time)
n = int(input())
lst = []
for i in range(1,n+1):
    a = ThongTin(i,input(),input(),input(),input())
    c = 1 
    for i in lst :
        if i.name == a.name :
            i.settime(a.time)
            i.setlm(a.lm)
            c = 0
            break
    if c==1 :
        lst.append(a)
for i in lst:
    print(i)